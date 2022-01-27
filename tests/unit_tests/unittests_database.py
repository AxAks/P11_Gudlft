"""
Tests file for researches in database
"""
import pytest
from lib_database.lib_database import get_club_by_email, get_club_by_name, get_competition_by_name, \
    convert_competition_places_to_int, convert_club_points_to_int


def test_load_clubs(test_club_as_list):
    """
    Checks that the list of clubs can be loaded from a json database file
    """
    assert len(test_club_as_list) == 1


def test_load_competitions(test_competitions_as_list):
    """
    Checks that the list of competitions can be loaded from a json database file
    """
    assert len(test_competitions_as_list) == 2


def test_a_registered_email_should_return_a_club(test_club_as_list, test_club):
    """
    Checks that a registered email is found
    """
    email = test_club['email']
    assert get_club_by_email(email, test_club_as_list) == test_club


def test_an_unregistered_email_should_return_none(test_club_as_list):
    """
    Checks that an unregistered email cannot be found
    """
    clubs = [club for club in test_club_as_list]
    email = 'unregistered_user@testclub.com'
    assert get_club_by_email(email, clubs) is None


def test_a_registered_club_name_should_return_the_matching_club(test_club_as_list, test_club):
    """
    Checks that a registered club name returns the club
    """
    club_name = test_club['name']
    assert get_club_by_name(club_name, test_club_as_list) == test_club


def test_an_unregistered_club_name_should_return_none(test_club_as_list):
    """
    Checks that an unregistered club name cannot be found
    """
    club_name = 'I am not a Club'
    assert get_club_by_name(club_name, test_club_as_list) is None


def test_a_registered_competition_name_should_return_the_matching_competition(test_competitions_as_list,
                                                                              test_future_competition):
    """
    Checks that a registered club name returns the club
    """
    competition_name = test_future_competition['name']
    assert get_competition_by_name(competition_name, test_competitions_as_list) == test_future_competition


def test_an_unregistered_competition_name_should_return_none(test_competitions_as_list):
    """
    Checks that an unregistered club name cannot be found
    """
    competition_name = 'I am not a Competition'
    assert get_competition_by_name(competition_name, test_competitions_as_list) is None


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
    competition_places = ''
    with pytest.raises(ValueError):
        assert convert_competition_places_to_int(competition_places)


def test_a_converted_competition_places_should_raise_value_error_if_negative():
    """
    Checks that the input can be converted into an integer
    """
    competition_places = '0'
    with pytest.raises(ValueError):
        assert convert_competition_places_to_int(competition_places)


def test_a_converted_club_points_should_return_a_int(test_club):
    """
    Checks that the input can be converted into an integer
    """
    club_points = test_club['points']
    assert isinstance(convert_club_points_to_int(club_points), int)


def test_a_converted_club_points_should_raise_value_error_if_empty():
    """
    Checks that the input can be converted into an integer
    """
    club_points = ''
    with pytest.raises(ValueError):
        assert convert_club_points_to_int(club_points)


def test_a_converted_club_points_should_raise_value_error_if_negative():
    """
    Checks that the input can be converted into an integer
    """
    club_points = '0'
    with pytest.raises(ValueError):
        assert convert_club_points_to_int(club_points)
