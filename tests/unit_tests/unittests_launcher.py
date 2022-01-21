"""
File for Unit Tests :

TDD approach :
1 🔴  Red : write a unit test that fails.
2 ✅  Green : write the source code that makes the test pass.
3 🛠  Refactor : refactor the source code to improve it.
"""
import pytest
from datetime import datetime

from lib_general.lib_general import check_club_points, check_competition_places, check_booking_possible, \
    check_competition_date, is_email_blank, check_required_places_amount

from .unittest_database import *  #  à modifier
from .unittest_requests import *  #  à modifier

"""
Extraire chaque tests dans un fichier nommé séparé, au fur et a mesure
"""


def test_index_with_registered_clubs(client, test_club_as_list, mocker_test_club_as_list):
    """
    checks that the route for index returns a success status code
    and displays the needed elements in template:
    - page title
    - points table for clubs
    """
    response = client.get('/')
    assert response.status_code == 200
    response_decode = response.data.decode()
    assert 'GUDLFT Registration Portal!' in response_decode
    assert 'Test Club' in response_decode
    assert '- 16' in response_decode


def test_index_with_no_clubs_registered(client, test_empty_list, mocker_test_empty_clubs_list):
    """
    checks that the route for index returns a success status code
    and displays that there is no club to display when clubs list in databases is empty
    """
    response = client.get('/')
    assert response.status_code == 200
    response_decode = response.data.decode()
    assert 'GUDLFT Registration Portal!' in response_decode
    assert 'No clubs to display' in response_decode


def test_show_summary_with_registered_competitions(client, test_competition_as_list, mocker_test_competition_as_list):
    """
    checks that the route for show summary returns a success status code
    and displays the list of registered competitions from databases
    """
    response = client.post('/show_summary', data={'email': 'john@simplylift.co'})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome, john@simplylift.co' in response_decode
    assert 'Test Competition' in response_decode


def test_show_summary_with_no_registered_competitions(client, test_empty_list, mocker_test_empty_competitions_list):
    """
    checks that the route for show summary returns a success status code
    and displays that there is no competition to display when competitions list in databases is empty
    """
    response = client.post('/show_summary', data={'email': 'john@simplylift.co'})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome, john@simplylift.co' in response_decode
    assert 'No competitions to display' in response_decode


def test_book(client):
    """

    """
    response = client.get('/book/<competition_name>/<club_name>',
                          data={'competition_name': 'Spring Festival', 'club_name': 'Iron Temple'})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Places' in response_decode


def test_purchase_places(client):
    """
    TDD : When a place for a competition is bought, the number of points is deduced
    """
    response = client.post('/purchase_places',
                           data={'competition': 'Fall Classic', 'club': 'Iron Temple', 'places': '2'})
    response_decode = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome, admin@irontemple.com' in response_decode


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
    assert check_competition_date(competition_date, now) is True


def test_competition_date_in_the_past_should_return_false():
    now = datetime.strptime("2022-01-02 09:00:00", "%Y-%m-%d %H:%M:%S")
    competition_date = datetime.strptime("2022-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
    assert check_competition_date(competition_date, now) is False


def test_places_required_below_limit_should_return_true():
    """

    """
    places_required_as_int = 12
    limit = 12
    assert check_required_places_amount(places_required_as_int, limit) is True


def test_places_required_above_limit_should_return_false():
    """

    """
    places_required_as_int = 13
    limit = 12
    assert check_required_places_amount(places_required_as_int, limit) is False


def test_places_ok_points_ok_competition_date_ok_places_below_limit_ok_should_return_true():
    """
    Must return True when every argument is true
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is True


def test_places_ok_points_ok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true but competition date
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_ok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true but amount of club points
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_ok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true but amount of available places in competition
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_ok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true except:
     - amount of club points
     - amount of available places in competition
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true except:
     - amount of available places in competition
     - valid competition date
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true except:
     - amount of club points
     - valid competition date
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when only the argument in limitation in places requested is true
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_ok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
     - the limitation in places requested
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_ok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
    - valid competition date
    - the limitation in places requested
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
    - clubs points
    - the limitation in places requested
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
    - available places in competition
    - the limitation in places requested
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when only the argument of competition date is true
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when only the argument in clubs points is true
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when only the argument in available places in competition is true
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when all arguments are false
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_logout(client):
    """

    """
    response = client.get('/logout')
    response_decode = response.data.decode()

    assert response.status_code == 302
    assert 'redirected automatically to target URL: <a href="/">/</a>' in response_decode
