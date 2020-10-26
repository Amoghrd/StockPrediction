import pytest
from flask import session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get("/auth/register").status_code == 200
    response = client.post("/auth/register", data={"username": "a", "password": "a"})
    assert "http://localhost/auth/login" == response.headers["Location"]

    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "select * from user where username = 'a'",
        )
        assert cursor.fetchone() is not None


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("a", "test", b"Incorrect username."),
        ("test", "a", b"Incorrect password."),
    ),
)
def test_logout(client, auth, username, password, message):
    auth.login(username, password)

    with client:
        auth.logout()
        assert "user_id" not in session
