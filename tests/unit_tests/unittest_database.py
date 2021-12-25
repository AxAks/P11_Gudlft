"""
Tests file for researches in database
"""
from lib_database.lib_database import get_club_by_email, get_club_by_name
from utils import load_database


def test_load_clubs():
    """
    Checks that the list of clubs can be loaded from a json database file
    """
    list_of_clubs = load_database('tests/db_for_tests.json')['clubs']  # test pas tres pertinent, à revoir
    assert list_of_clubs is not None


def test_load_competitions(client): # test pas tres pertinent, à revoir
    """
    Checks that the list of competitions can be loaded from a json database file
    """
    competitions = load_database('tests/db_for_tests.json')['competitions']
    assert competitions is not None


def test_a_registered_email_should_return_a_club():
    """
    Checks that a registered email is found
    """
    email = "john@simplylift.co"
    assert get_club_by_email(email) is not None


def test_an_unregistered_email_should_return_none():
    """
    Checks that an unregistered email cannot be found
    """
    email = 'unregistered_user@testclub.com'
    assert get_club_by_email(email) is None


def test_a_malformed_email_address_should_not_be_accepted(): # ??
    """

    """
    assert True is False
    email = 'malformed_address@testclub.co'
    pass


def test_a_registered_club_name_should_return_the_matching_club():
    """
    Checks that a registered club name returns the club
    """
    club_name = "Iron Temple"
    assert get_club_by_name(club_name) is not None


def test_an_unregistered_club_name_should_return_none():
    """
    Checks that an unregistered club name cannot be found
    """
    club_name = 'I am not a Club'
    assert get_club_by_email(club_name) is None
