"""
File for Unit Tests :

TDD approach :
1 🔴  Red : write a unit test that fails.
2 ✅  Green : write the source code that makes the test pass.
3 🛠  Refactor : refactor the source code to improve it.
"""
import pytest
from datetime import datetime
import config
import utils
from lib_general.lib_general import check_club_points, check_competition_places, check_booking_possible, \
    check_competition_date

from unittest_database import *  # à modifier
from unittest_requests import *  # à modifier


"""
Extraire chaque tests dans un fichier nommé séparé, au fur et a mesure
"""


@pytest.fixture  # simulation de client pour les requests, à revoir ...
def client():
    tested_app = config.app
    test_db = 'tests/db_for_tests.json'
    with tested_app.test_client() as client:
        with tested_app.app_context():
            utils.load(test_db)
        yield client


def test_index():
    """

    """
    assert True is False
    pass


def test_book():
    """

    """
    assert True is False
    pass


def test_purchase_places():
    """
    TDD : When a place for a competition is bought, the number of points is deduced
    """
    assert False is True


def test_enough_places_in_competition_should_return_true():
    places_required_as_int = 6
    total_places_in_competition_as_int = 25
    assert check_competition_places(places_required_as_int, total_places_in_competition_as_int) is True


def test_not_enough_places_in_competition_should_return_false():
    places_required_as_int = 26
    total_places_in_competition_as_int = 25
    assert check_competition_places(places_required_as_int, total_places_in_competition_as_int) is False


def test_enough_points_for_club_should_return_true():
    places_required_as_int = 13
    total_club_points_as_int = 13
    assert check_club_points(places_required_as_int, total_club_points_as_int) is True


def test_not_enough_points_for_club_should_return_false():
    places_required_as_int = 14
    total_club_points_as_int = 13
    assert check_club_points(places_required_as_int, total_club_points_as_int) is False


def test_competition_date_in_the_future_should_return_true():
    now = datetime.strptime("2022-01-02 09:00:00", "%Y-%m-%d %H:%M:%S")
    competition_date = datetime.strptime("2022-03-12 10:00:00", "%Y-%m-%d %H:%M:%S")
    assert check_competition_date(competition_date) is True  # il faut mocker le now ...


def test_competition_date_in_the_past_should_return_false():
    now = datetime.strptime("2022-01-02 09:00:00", "%Y-%m-%d %H:%M:%S")
    competition_date = datetime.strptime("2022-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
    assert check_competition_date(competition_date) is False  # il faut mocker le now ...


def test_places_ok_points_ok_competition_date_ok_should_return_true():
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = True
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is True


def test_places_ok_points_ok_competition_date_nok_should_return_false():
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = False
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is False


def test_places_ok_points_nok_competition_date_ok_should_return_false():
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = True
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is False


def test_places_nok_points_ok_competition_date_ok_should_return_false():
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = True
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is False


def test_places_nok_points_nok_competition_date_ok_should_return_false():
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = True
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is False


def test_places_nok_points_ok_competition_date_nok_should_return_false():
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = False
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is False


def test_places_ok_points_nok_competition_date_nok_should_return_false():
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = False
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is False


def test_places_nok_points_nok_competition_date_nok_should_return_false():
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = False
    assert check_booking_possible(has_enough_places, has_enough_points, competition_is_in_the_future) is False


def test_display_points():
    """

    """
    assert True is False
    pass


def test_logout():
    """

    """
    assert True is False
    pass
