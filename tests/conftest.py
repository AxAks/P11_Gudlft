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
    test_database = {
        "clubs": [
            {
                "name": "Test Club",
                "email": "test@club.com",
                "points": "16"
            },
        ],
        "competitions": [
            {
                "name": "Test Competition",
                "date": "2022-03-22 10:00:00",
                "number_of_places": "20"
            },
        ]
    }
    return test_database


@pytest.fixture
def mocker_test_database(mocker, test_database):
    mocker.patch.object(server, 'database', test_database)


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
    clubs = [
        {
            "name": "Test Club",
            "email": "test@club.com",
            "points": "16"
        },
    ]
    return clubs


@pytest.fixture
def mocker_test_club_as_list(mocker, test_club_as_list):
    mocker.patch.object(server, 'clubs', test_club_as_list)


@pytest.fixture
def mocker_test_empty_clubs_list(mocker, test_empty_list):
    mocker.patch.object(server, 'clubs', test_empty_list)


@pytest.fixture
def test_club():
    return {
        "name": "Test Club",
        "email": "test@club.com",
        "points": "16"
    }


@pytest.fixture
def mocker_test_club(mocker, test_club):
    mocker.patch.object(server, 'clubs', test_club)


@pytest.fixture
def test_competition_as_list():
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
def mocker_test_competition_as_list(mocker, test_competition_as_list):
    mocker.patch.object(server, 'competitions', test_competition_as_list)


@pytest.fixture
def mocker_test_empty_competitions_list(mocker, test_empty_list):
    mocker.patch.object(server, 'competitions', test_empty_list)


@pytest.fixture
def test_competition():
    return {
        "name": "Test Competition",
        "date": "2022-03-22 10:00:00",
        "number_of_places": "20"
    }


@pytest.fixture
def mocker_test_competition(mocker, test_competition):
    mocker.patch.object(server, 'competitions', test_competition)


@pytest.fixture
def test_required_places():
    """
    Returns a lambda amount of required places for tests purpose
    """
    return '6'
