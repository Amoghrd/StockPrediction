import click
from flask import current_app, g
from flask.cli import with_appcontext
import mysql.connector


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def get_db():
    connection = mysql.connector.connect(
        host="seng2021.csbfa4eylzxn.us-east-2.rds.amazonaws.com",
        database="StockPrediction",
        user="root",
        password="SEFall2021",
    )
    return connection


def init_db():
    db = get_db()
    cursor = db.cursor()

    with current_app.open_resource("schema.sql") as f:
        cursor.execute(f.read().decode("utf-8"), multi=True)


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
