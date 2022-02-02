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
def test_database():
    return {'clubs': [
        {
            "name": "Test Club",
            "email": "test@club.com",
            "points": "18"
        },
        {
            "name": "Test Club not enough points",
            "email": "test@club.com",
            "points": "18"
        },
        {
            "name": "Test registered Club",
            "email": "registered@club.com",
            "points": "18"
        }
    ],
        'competitions': [
            {
                "name": "Test Past Competition",
                "date": "2020-03-22 10:00:00",
                "number_of_places": "18"
            },
            {
                "name": "Test Future Competition",
                "date": "2022-03-22 10:00:00",
                "number_of_places": "20"
            },
            {
                "name": "Test Future Competition not enough points",
                "date": "2022-03-22 10:00:00",
                "number_of_places": "20"
            }
        ]
    }


@pytest.fixture
def test_bookings_registry():
    return {
        "Test Club": [
            {"Test Past Competition": 0},
            {"Test Future Competition": 0},
            {"Test Future Competition not enough points": 0}
        ],
        "Test Club not enough points": [
            {"Test Past Competition": 0},
            {"Test Future Competition": 0},
            {"Test Future Competition not enough points": 0}
        ],
        "Test registered Club": [
            {"Test Past Competition": 0},
            {"Test Future Competition": 6},
            {"Test Future Competition not enough points": 0}
        ]
    }


@pytest.fixture
def test_db_path():
    return 'tests/test_db.json'


@pytest.fixture
def test_empty_list():
    """
    Returns an empty list for registered elements in database for tests purpose
    """
    return []


@pytest.fixture
def test_club_as_list():
    """
    Returns a lambda club as list for tests purpose
    """
    return [
        {
            "name": "Test Club",
            "email": "test@club.com",
            "points": "18"
        },
        {
            "name": "Test Club not enough points",
            "email": "test@club.com",
            "points": "18"
        },         {
            "name": "Test registered Club",
            "email": "registered@club.com",
            "points": "18"
        }
    ]


@pytest.fixture
def test_club():
    return {
        "name": "Test Club",
        "email": "test@club.com",
        "points": "18"
    }


@pytest.fixture
def test_registered_club():
    return {
        "name": "Test registered Club",
        "email": "registered@club.com",
        "points": "18"
    }


@pytest.fixture
def test_not_registered_club():
    return {
        "name": "I do not exist Club",
        "email": "not_registered@club.com",
        "points": "18"
    }


@pytest.fixture
def test_club_not_enough_points():
    return {
        "name": "Test Club not enough points",
        "email": "test@club.com",
        "points": "18"
    }


@pytest.fixture
def test_competitions_as_list():
    """
    Returns a lambda competition for tests purpose
    """
    return [
        {
            "name": "Test Past Competition",
            "date": "2020-03-22 10:00:00",
            "number_of_places": "18"
        },
        {
            "name": "Test Future Competition",
            "date": "2022-03-22 10:00:00",
            "number_of_places": "20"
        },
        {
            "name": "Test Future Competition not enough points",
            "date": "2022-03-22 10:00:00",
            "number_of_places": "20"
        }
    ]


@pytest.fixture
def test_future_competition():
    return {
        "name": "Test Future Competition",
        "date": "2022-03-22 10:00:00",
        "number_of_places": "20"
    }


@pytest.fixture
def test_future_competition_not_enough_points():
    return {
        "name": "Test Future Competition not enough points",
        "date": "2022-03-22 10:00:00",
        "number_of_places": "20"
    }


@pytest.fixture
def test_requested_places_6():
    """
    Returns a lambda amount of required places for tests purpose
    """
    return '6'


@pytest.fixture
def test_requested_places_9():
    """
    Returns a lambda amount of requested places for tests purpose
    """
    return '9'


@pytest.fixture
def test_requested_places_6_as_int():
    """
    Returns a lambda amount of requested places for tests purpose
    """
    return 6


@pytest.fixture
def test_requested_places_12_as_int():
    """
    Returns a lambda amount of requested places for tests purpose
    """
    return 12


@pytest.fixture
def test_requested_places_13_as_int():
    """
    Returns a lambda amount of requested places for tests purpose
    """
    return 13


@pytest.fixture
def test_requested_booking_limit_12():
    """
    Returns a lambda amount of requested places for tests purpose
    """
    return 12


@pytest.fixture
def test_needed_amount_of_points_18():
    """
    Returns a lambda amount of needed points for tests purpose
    """
    return 18


@pytest.fixture
def test_requested_places_9_as_int():
    """
    Returns a lambda amount of requested places for tests purpose
    """
    return 9


@pytest.fixture
def test_needed_amount_of_points_27():
    """
    Returns a lambda amount of needed points for tests purpose
    """
    return 27


@pytest.fixture
def mocker_test_database(mocker, test_database):
    mocker.patch.object(server, 'database', test_database)


@pytest.fixture
def mocker_test_db_path(mocker, test_db_path):
    mocker.patch.object(server, 'db_path', test_db_path)


@pytest.fixture
def mocker_test_bookings_registry(mocker, test_bookings_registry):
    mocker.patch.object(server, 'bookings_registry', test_bookings_registry)


@pytest.fixture
def mocker_test_club_as_list(mocker, test_club_as_list):
    mocker.patch.object(server, 'clubs', test_club_as_list)


@pytest.fixture
def mocker_test_empty_clubs_list(mocker, test_empty_list):
    mocker.patch.object(server, 'clubs', test_empty_list)


@pytest.fixture
def mocker_test_competitions_as_list(mocker, test_competitions_as_list):
    mocker.patch.object(server, 'competitions', test_competitions_as_list)


@pytest.fixture
def mocker_test_empty_competitions_list(mocker, test_empty_list):
    mocker.patch.object(server, 'competitions', test_empty_list)
