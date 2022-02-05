"""
File for Unit Tests in route purchase_places
"""
from typing import Dict, List

import pytest

from libs.lib_purchase_places import extract_club_name, extract_competition_name, extract_requested_places, \
    check_competition_places, check_club_points, check_required_places_amount, check_booking_possible, book_places, \
    convert_competition_places_to_int, convert_club_points_to_int, spot_club_bookings_field_in_registry, \
    calculate_total_desired_places, extract_nb_booked_places_for_competition, calculate_required_points, \
    update_and_get_booked_places_in_registry


def test_an_entered_competition_name_should_return_a_string(test_future_competition):
    """
    Checks that the input is a valid string
    """
    form = {'competition_name': test_future_competition['name']}
    assert 'competition_name' in form.keys()
    assert isinstance(extract_competition_name(form), str)


def test_an_empty_competition_name_should_return_an_empty_string():
    """
    Checks that the input is a valid string
    """
    empty_form = {'competition_name': ''}
    assert 'competition_name' in empty_form.keys()
    assert extract_competition_name(empty_form) == ''


def test_a_converted_competition_places_should_return_a_int(test_future_competition):
    """
    Checks that the input can be converted into an integer
    """
    competition_places = test_future_competition['number_of_places']
    assert isinstance(convert_competition_places_to_int(competition_places), int)


def test_a_converted_competition_places_should_raise_value_error_if_empty():
    """
    Checks that the input can be converted into an integer
    """
    with pytest.raises(ValueError):
        assert convert_competition_places_to_int('')


def test_a_converted_competition_places_should_raise_value_error_if_negative():
    """
    Checks that the input can be converted into an integer
    """
    with pytest.raises(ValueError):
        assert convert_competition_places_to_int('0')


def test_a_converted_club_points_should_return_a_int():
    """
    Checks that the input can be converted into an integer
    """
    assert isinstance(convert_club_points_to_int('12'), int)


def test_a_converted_club_points_should_raise_value_error_if_empty():
    """
        Checks that an empty string input raises a ValueError
    """
    with pytest.raises(ValueError):
        assert convert_club_points_to_int('')


def test_a_converted_club_points_should_raise_value_error_if_negative():
    """
    Checks that a negative string input raises a ValueError
    """
    with pytest.raises(ValueError):
        assert convert_club_points_to_int('0')


def test_enough_points_for_club_should_return_true():
    assert check_club_points(13, 13) is True


def test_not_enough_points_for_club_should_return_false():
    assert check_club_points(14, 13) is False


def test_enough_places_in_competition_should_return_true():

    assert check_competition_places(6, 25) is True


def test_not_enough_places_in_competition_should_return_false():
    assert check_competition_places(26, 25) is False


def test_an_entered_club_name_should_return_a_string(test_club):
    """
    Checks that the input is a valid string
    """
    form = {'club_name': test_club['name']}
    assert 'club_name' in form.keys()
    assert isinstance(extract_club_name(form), str)


def test_an_empty_club_name_should_return_an_empty_string():
    """
    Checks that the input is a valid string
    """
    form = {'club_name': ''}
    assert 'club_name' in form.keys()
    assert extract_club_name(form) == ''


def test_an_entered_amount_of_places_should_return_a_int():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': '2'}
    assert 'places' in form.keys()
    assert isinstance(extract_requested_places(form), int)


def test_an_empty_amount_of_places_should_raise_a_value_error():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': ''}
    assert 'places' in form.keys()
    with pytest.raises(ValueError):
        extract_requested_places(form)


def test_a_negative_amount_of_places_should_raise_a_value_error():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': '0'}
    assert 'places' in form.keys()
    with pytest.raises(ValueError):
        extract_requested_places(form)


def test_calculate_required_points():
    """
    Checks that the conversion from number of places to number of points needed works
    """
    assert calculate_required_points(6) == 18


def test_extract_nb_booked_places_for_competition(test_bookings_future_6_places_dict, test_future_competition):
    """
    Checks that the number of places already booked by a club for a competition
    can be extracted from an entry in booking registry
    """
    assert extract_nb_booked_places_for_competition(test_bookings_future_6_places_dict,
                                                    test_future_competition) == 6


def test_spot_club_bookings_field_in_registry_with_registered_club_and_competition(test_bookings_registry,
                                                                                   test_registered_club,
                                                                                   test_future_competition):
    """
    checks that the function returns a "competition/nb_of_points_booked" dict for a club
    when the club and the competition exist in the registry
    """
    assert spot_club_bookings_field_in_registry(test_bookings_registry,
                                                test_registered_club,
                                                test_future_competition) == {'Test Future Competition': 6}


def test_spot_club_bookings_field_club_not_in_registry(test_bookings_registry,
                                                       test_not_registered_club,
                                                       test_future_competition):
    """
    checks that the function handles the case when a club is not found in registry
    (raises an exception if the club is not found ?)
    """
    with pytest.raises(KeyError):
        spot_club_bookings_field_in_registry(test_bookings_registry,
                                             test_not_registered_club,
                                             test_future_competition)


def test_spot_club_bookings_field_competition_not_in_registry(test_bookings_registry,
                                                              test_registered_club,
                                                              test_not_registered_competition):
    """
    checks that the function handles the case when a club is not found in registry
    (raises an exception if the competition is not found ?)
    """
    with pytest.raises(KeyError):
        spot_club_bookings_field_in_registry(test_bookings_registry,
                                             test_registered_club,
                                             test_not_registered_competition)


def test_calculate_total_desired_places():
    """
    Checks that sum of registered places already booked by the club for a competition
    and the new request of places for the same competition returns the right total of requested places
    """
    assert calculate_total_desired_places(6, 6) == 12


def test_update_and_get_booked_places_in_registry(test_bookings_registry: Dict[str, List[Dict[str, int]]],
                                                  test_club: Dict,
                                                  test_future_competition: Dict):
    """
    assert update_and_get_booked_places_in_registry(
    """
    assert update_and_get_booked_places_in_registry(test_bookings_registry,
                                                    test_club,
                                                    test_future_competition, 12) == {'Test Future Competition': 12}


def test_places_required_below_limit_should_return_true():
    """
    Checks that the function returns True when the requested amount of places
    is under the limit of 12 per competition for a club
    """
    assert check_required_places_amount(12, 12) is True


def test_places_required_above_limit_should_return_false():
    """
    Checks that the function returns False when the requested amount of places
    is above the limit of 12 per competition for a club
    """
    assert check_required_places_amount(13, 12) is False


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


def test_book_places(test_club, test_future_competition):
    """
    nominal case
    """
    total_places_as_int = int(test_future_competition['number_of_places'])
    total_points_as_int = int(test_club['points'])
    updated_club, updated_competition = book_places(test_club, test_future_competition,
                                                    6, total_places_as_int,
                                                    18, total_points_as_int)
    assert updated_club['points'] == "0"
    assert updated_competition['number_of_places'] == "14"
