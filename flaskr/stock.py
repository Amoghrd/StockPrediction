from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    session,
)

from flaskr.auth import login_required
from flaskr.db import get_db
import csv
from datetime import date
from flaskr.fetch_data import get_stock
from flaskr.fetch_data import regression

from flask_table import Table, Col


# Declare your table
class ItemTable(Table):
    name = Col("Name")
    ticker = Col("Ticker")
    slope = Col("Slope")


# Get some objects
class Item(object):
    def __init__(self, name, ticker, slope):
        self.name = name
        self.ticker = ticker
        self.slope = slope


contains = set()

bp = Blueprint("stock", __name__)


@bp.route("/")
def home():
    return redirect(url_for("auth.login"))


@bp.route("/index")
@login_required
def index():
    db = get_db()
    cursor = db.cursor()
    # I created a method in this file get_post() which gets all the ticker names from
    # stock_id, which is currently just amazon.
    # posts = get_post()
    # You need to do the following - for each stock_id in posts, call the fetch_data
    # function, save the matplotlib chart image into static folder with the filename
    # format COMAPNYNAME-DD-MM-YY for the date upto which model has been made.
    # Now populate the below list(of lists) with ['COMPANYNAME','FILENAME'] for each
    # company, format which will be read at website.
    # This is all static to represent working
    cursor.execute("Select * from stock")
    if len(cursor.fetchall()) == 0:
        with open("flaskr/static/stocks.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    cursor.execute(
                        "INSERT INTO stock (stock_name,stock_id) VALUES(%s,%s)",
                        (row[1], row[0]),
                    )
                    db.commit()
                except Exception as e:
                    print(e)
    posts = get_post()
    info_stocks = []
    for item in posts:
        print("xxxx" + item[0])
        df = get_stock(item[0], 200)
        # calling linear regression functiom
        regression(df, item[0], date.today().strftime("%d-%m-%Y"))
        info_stocks.append(
            [item[0], item[0] + "-" + date.today().strftime("%d-%m-%Y") + ".png"]
        )
    print(info_stocks)
    # info_stocks = [['AMZN', 'AMZN-DD-MM-YY.png']]
    return render_template("stock/index.html", posts=info_stocks, table=populateTable())


@bp.route("/choose", methods=("POST", "GET"))
@login_required
def choose():
    if request.method == "POST":
        stock_name = request.form["stock_name"]
        error = None

        if not stock_name:
            error = "Stock Name is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            cursor = db.cursor()
            try:
                print("Got Ticker", stock_name)
                cursor.execute(
                    "SELECT stock_id FROM stock WHERE stock_name = %s", (stock_name,)
                )
                stock_id = cursor.fetchone()
                # The API which gets data from internet does not take company name for
                # getting data, but rather ticker for the company.
                # For example Amazon has ticker AMZN, Apple AAPL, so gather a list from
                # internet which gives you this conversion.
                # Then u need to store those into stock_id column of stock table
                # corresponding to each company.
                if (stock_id, session.get("username")) in contains:
                    db.commit()
                else:
                    contains.add((stock_id, session.get("username")))
                    cursor.execute(
                        "INSERT INTO user_stock (stock_id,username)" " VALUES (%s,%s)",
                        (stock_id[0], session.get("username")),
                    )
                    # Currently I am just storing AMZN only to represent, you can
                    # modify it back to previous way after you are able to get
                    # correct tickers.
                    db.commit()

            except Exception as e:
                print(e)
            return redirect(url_for("stock.index"))

    return render_template("stock/choose.html")


def get_post():
    try:
        print(session.get("username"))
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT stock_id from user_stock WHERE username = %s",
            (session.get("username"),),
        )
        post = cursor.fetchall()
        print(post)
    except Exception as e:
        print(e)
    return post


def populateTable():
    topTen1 = []
    topTen2 = []
    with open("flaskr/GrowthRates.csv") as f:
        reader = csv.reader(f)
        i = 10
        for row in reader:
            if i == 0:
                break
            topTen1.append(Item(row[1], row[0], row[2]))
            topTen2.append([row[1], row[0], row[2]])
            i -= 1

    # Populate the table
    table = ItemTable(topTen1)
    table = topTen2

    return table
