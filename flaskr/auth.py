import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

import click

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        cursor = db.cursor()
        error = None
        check_user_sql = "SELECT * FROM user where username = %s"
        user = (username,)
        cursor.execute(check_user_sql, user)
        user = cursor.fetchone()

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif user is not None:
            error = "User {} is already registered.".format(username)

        if error is None:
            sql = "INSERT INTO user(username, password) VALUES(%s,%s)"
            data = (username, generate_password_hash(password))
            cursor.execute(sql, data)
            db.commit()
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        cursor = db.cursor()
        error = None
        sql = "SELECT * FROM user where username = %s"
        user = (username,)
        cursor.execute(sql, user)
        user = cursor.fetchone()

        if user is None:
            error = "Incorrect username."
            # calling check_password_hash function
        elif not check_password_hash(user[1], password):
            click.echo(user[0])
            click.echo(user[1])
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["username"] = user[0]
            return redirect(url_for("stock.index"))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


@bp.before_app_request
def load_logged_in_user():
    username = session.get("username")

    if username is None:
        g.user = None
    else:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        g.user = cursor.fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view
