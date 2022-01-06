"""
Tests file for researches in database
"""
from lib_database.lib_database import get_club_by_email, get_club_by_name
from tests.conftest import test_club, test_competition
from utils import load


def test_load_clubs(test_club):
    """
    Checks that the list of clubs can be loaded from a json database file
    """
    assert len(test_club) == 1


def test_load_competitions(test_competition):
    """
    Checks that the list of competitions can be loaded from a json database file
    """
    assert len(test_competition) == 1


def test_a_registered_email_should_return_a_club(test_club):  # test not working
    """
    Checks that a registered email is found
    """
    email = "test@club.com"
    assert len(get_club_by_email(email, test_club)) == 1


def test_an_unregistered_email_should_return_none(test_club):  # test not working
    """
    Checks that an unregistered email cannot be found
    """
    email = 'unregistered_user@testclub.com'
    assert get_club_by_email(email, test_club) is None


def test_a_registered_club_name_should_return_the_matching_club():
    """
    Checks that a registered club name returns the club
    """
    club_name = "Iron Temple"
    assert get_club_by_name(club_name, test_club) is not None


def test_an_unregistered_club_name_should_return_none():
    """
    Checks that an unregistered club name cannot be found
    """
    club_name = 'I am not a Club'
    assert get_club_by_email(club_name, test_club) is None   # test not working
