import pytest
from flask import session


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
