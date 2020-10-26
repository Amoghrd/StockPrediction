import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert 'http://localhost/auth/login' == response.headers['Location']

    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "select * from user where username = 'a'",
        )
        assert cursor.fetchone() is not None

