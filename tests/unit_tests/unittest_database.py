"""
Tests file for researches in database
"""
from lib_database.lib_database import get_club_by_email
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
    # si l'adresse est dans la base : OK
    # si l'adresse n'est pas dans la base : NOK

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
    email = 'malformed_address@testclub.co'
    pass
