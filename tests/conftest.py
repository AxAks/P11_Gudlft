"""
Tests Conf File for pytest
"""
import pytest
from typing import Dict, List

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
def test_database() -> Dict[str, List[Dict]]:
    """

    """
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
def test_bookings_registry() -> Dict[str, List[Dict]]:
    """

    """
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
def test_db_path() -> str:
    """

    """
    return 'tests/test_db.json'


@pytest.fixture
def test_empty_list() -> List:
    """
    Returns an empty list for registered elements in database for tests purpose
    """
    return []


@pytest.fixture
def test_club_as_list() -> List[Dict]:
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
        }, {
            "name": "Test registered Club",
            "email": "registered@club.com",
            "points": "18"
        }
    ]


@pytest.fixture
def test_club() -> Dict:
    """

    """
    return {
        "name": "Test Club",
        "email": "test@club.com",
        "points": "18"
    }


@pytest.fixture
def test_registered_club() -> Dict:
    """

    """
    return {
        "name": "Test registered Club",
        "email": "registered@club.com",
        "points": "18"
    }


@pytest.fixture
def test_not_registered_club() -> Dict:
    """

    """
    return {
        "name": "I do not exist Club",
        "email": "not_registered@club.com",
        "points": "18"
    }


@pytest.fixture
def test_club_not_enough_points() -> Dict:
    """

    """
    return {
        "name": "Test Club not enough points",
        "email": "test@club.com",
        "points": "18"
    }


@pytest.fixture
def test_competitions_as_list() -> List[Dict]:
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
def test_future_competition() -> Dict:
    """

    """
    return {
        "name": "Test Future Competition",
        "date": "2022-03-22 10:00:00",
        "number_of_places": "20"
    }


@pytest.fixture
def test_future_competition_not_enough_points() -> Dict:
    """

    """
    return {
        "name": "Test Future Competition not enough points",
        "date": "2022-03-22 10:00:00",
        "number_of_places": "20"
    }


@pytest.fixture
def test_club_points_12_as_str() -> str:
    return '12'


@pytest.fixture
def test_club_points_0_as_str() -> str:
    return '0'


@pytest.fixture
def test_club_points_empty_str() -> str:
    return ''


@pytest.fixture
def test_competition_places_0_as_str() -> str:
    return '0'


@pytest.fixture
def test_competition_places_empty_str() -> str:
    return ''


@pytest.fixture
def test_requested_places_6() -> str:
    """
    Returns a lambda amount of required places for tests purpose
    """
    return '6'


@pytest.fixture
def test_requested_places_9() -> str:
    """
    Returns 9 as a string as amount of requested places for a competition
    """
    return '9'


@pytest.fixture
def test_requested_places_6_as_int() -> int:
    """
    Returns 6 as amount of requested places to a competiton
    """
    return 6


@pytest.fixture
def test_requested_places_12_as_int() -> int:
    """
    Returns 12 as amount of requested places to a competiton
    """
    return 12


@pytest.fixture
def test_requested_places_13_as_int() -> int:
    """
    Returns 13 as amount of requested places to a competiton
    """
    return 13


@pytest.fixture
def test_requested_places_14_as_int() -> int:
    """
    Returns 14 as amount of requested places to a competiton
    """
    return 14


@pytest.fixture
def test_total_club_points_13_as_int() -> int:
    """
    Returns 13 as amount of requested places to a competiton
    """
    return 13


@pytest.fixture
def test_requested_places_26_as_int() -> int:
    """
    Returns 26 as amount of requested places to a competiton
    """
    return 26


@pytest.fixture
def test_total_places_in_competition_25_as_int() -> int:
    """
    Returns 25 as total available places in a competition
    """
    return 25


@pytest.fixture
def test_requested_booking_limit_12() -> int:
    """
    Returns 12 as limit of places to a competition per club
    """
    return 12


@pytest.fixture
def test_needed_amount_of_points_18() -> int:
    """
    Returns 18 as amount of needed points to book a given number of places to a competition
    """
    return 18


@pytest.fixture
def test_requested_places_9_as_int() -> int:
    """
    Returns 9 as amount of requested places to a competiton
    """
    return 9


@pytest.fixture
def test_needed_amount_of_points_27() -> int:
    """
    Returns 27 as amount of needed points to book a given number of places to a competition
    """
    return 27


@pytest.fixture
def test_bookings_future_6_places_dict() -> Dict[str, int]:
    """
    Returns a dict {club name: booked_places} that simulates an entry in bookings registry
    """
    return {"Test Future Competition": 6}


@pytest.fixture()
def test_nb_already_booked_places_6() -> int:
    """
    Returns 6 to simulate a extraction of already booked placs from an entry in bookings registry
    """


@pytest.fixture
def mocker_test_database(mocker, test_database):
    """
    Enables to mock the database
    """
    mocker.patch.object(server, 'database', test_database)


@pytest.fixture
def mocker_test_db_path(mocker, test_db_path):
    """
    Enables to mock the database path
    and then interact with a alternative JSON File as database during test phases
    """
    mocker.patch.object(server, 'db_path', test_db_path)


@pytest.fixture
def mocker_test_bookings_registry(mocker, test_bookings_registry):
    """
    Enables to mock the bookings registry
    """
    mocker.patch.object(server, 'bookings_registry', test_bookings_registry)


@pytest.fixture
def mocker_test_club_as_list(mocker, test_club_as_list):
    """
    Enables to mock clubs with test values
    """
    mocker.patch.object(server, 'clubs', test_club_as_list)


@pytest.fixture
def mocker_test_empty_clubs_list(mocker, test_empty_list):
    """
    Enables to mock clubs with an empty list
    """
    mocker.patch.object(server, 'clubs', test_empty_list)


@pytest.fixture
def mocker_test_competitions_as_list(mocker, test_competitions_as_list):
    """
    Enables to mock competitions with test values
    """
    mocker.patch.object(server, 'competitions', test_competitions_as_list)


@pytest.fixture
def mocker_test_empty_competitions_list(mocker, test_empty_list):
    """
    Enables to mock competitions with an empty list
    """
    mocker.patch.object(server, 'competitions', test_empty_list)
