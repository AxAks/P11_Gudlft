"""
Tests Conf File for pytest
"""
import pytest
import server


@pytest.fixture
def app():
    tested_app = server.app
    with tested_app.app_context():
        yield tested_app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_club():  # j'arrive pas à l'utiliser
    """
    Returns a lambda club for tests purpose
    """
    clubs = [
        {
            "name": "Test Club",
            "email": "test@club.com",
            "points": "16"
        },
    ]
    return clubs


@pytest.fixture
def test_competition():  # j'arrive pas à l'utiliser
    """
    Returns a lambda competition for tests purpose
    """
    competitions = [
        {
            "name": "Test Competition",
            "date": "2022-03-22 10:00:00",
            "number_of_places": "20"
        },
    ]
    return competitions
