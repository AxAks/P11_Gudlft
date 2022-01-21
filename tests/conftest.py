"""
Tests Conf File for pytest
"""
from datetime import datetime

import pytest

import server
from models.clubs import Club
from models.competitions import Competition


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
def test_club_as_list():
    """
    Returns a lambda club for tests purpose
    """
    return [Club(name="Test Club", email="test@club.com", points=16)]


@pytest.fixture
def test_club_as_obj():
    """
    Returns a lambda club for tests purpose
    """
    return Club(name="Test Club", email="test@club.com", points=16)


@pytest.fixture
def test_empty_list():
    """
    Returns an empty list for registered elements in database for tests purpose
    """
    return []


@pytest.fixture
def test_new_club_points():
    """
    Returns an empty list for registered elements in database for tests purpose
    """
    return 5


@pytest.fixture
def test_new_competition_places():
    """
    Returns an empty list for registered elements in database for tests purpose
    """
    return 6


@pytest.fixture
def mocker_test_club_as_list(mocker, test_club_as_list):
    mocker.patch.object(server, 'clubs', test_club_as_list)


@pytest.fixture
def mocker_test_empty_clubs_list(mocker, test_empty_list):
    mocker.patch.object(server, 'clubs', test_empty_list)


@pytest.fixture
def test_competition_as_list():
    """
    Returns a lambda competition for tests purpose
    """
    return [Competition(name="Test Competition",
                        date=datetime.strptime("2022-03-22 10:00:00", '%Y-%m-%d %H:%M:%S'), number_of_places=20)]


@pytest.fixture
def test_competition_as_obj():
    """
    Returns a lambda competition for tests purpose
    """
    return Competition(name="Test Competition",
                       date=datetime.strptime("2022-03-22 10:00:00", '%Y-%m-%d %H:%M:%S'), number_of_places=20)


@pytest.fixture
def mocker_test_competition_as_list(mocker, test_competition_as_list):
    mocker.patch.object(server, 'competitions', test_competition_as_list)


@pytest.fixture
def mocker_test_empty_competitions_list(mocker, test_empty_list):
    mocker.patch.object(server, 'competitions', test_empty_list)


@pytest.fixture
def test_required_places():
    """
    Returns a lambda amount of required places for tests purpose
    """
    return '6'
