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
def test_club():
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
def test_empty_clubs_list():
    """
    Returns an empty list for registered clubs for tests purpose
    """
    clubs = []
    return clubs


@pytest.fixture
def mocker_test_club(mocker, test_club):
    mocker.patch.object(server, 'clubs', test_club)


@pytest.fixture
def mocker_test_empty_clubs_list(mocker, test_empty_clubs_list):
    mocker.patch.object(server, 'clubs', test_empty_clubs_list)


@pytest.fixture
def test_competition():
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


@pytest.fixture
def test_required_places():
    """
    Returns a lambda amount of required places for tests purpose
    """
    return '6'
