"""
Tests file for researches in databases
"""
from lib_database.lib_database import get_club_by_email, get_club_by_name, update_competition_places, \
    update_club_points
from models.clubs import Club


def test_load_clubs(test_club_as_list): # test à réécrire
    """
    Checks that the list of clubs can be loaded from a json databases file
    """
    assert len(test_club_as_list) == 1


def test_load_competitions(test_competition_as_list): # test à réécrire
    """
    Checks that the list of competitions can be loaded from a json databases file
    """
    assert len(test_competition_as_list) == 1


def test_a_registered_email_should_return_a_club(test_database, test_club_as_obj):
    """
    Checks that a registered email is found
    """
    email = "test@club.com"
    assert get_club_by_email(email) == test_club_as_obj  # les deux semblent identiques !!! mais ca retourne un AssertError quand meme !


def test_an_unregistered_email_should_return_none(test_database):
    """
    Checks that an unregistered email cannot be found
    """
    email = 'unregistered_user@testclub.com'
    assert get_club_by_email(email) is None


def test_a_registered_club_name_should_return_the_matching_club(test_database, test_club_as_obj):
    """
    Checks that a registered club name returns the club
    """
    club_name = "Test Club"
    assert get_club_by_name(club_name) == test_club_as_obj


def test_an_unregistered_club_name_should_return_none(test_database):
    """
    Checks that an unregistered club name cannot be found
    """
    club_name = 'I am not a Club'
    assert get_club_by_email(club_name) is None


def test_update_competition_places(test_database, test_competition_as_obj, test_new_competition_places):
    updated_competition = update_competition_places(test_competition_as_obj, test_new_competition_places)
    assert updated_competition.number_of_places >= 0


def test_update_club_points(test_database, test_club_as_obj, test_new_club_points):
    updated_club = update_club_points(test_club_as_obj, test_new_club_points)
    assert updated_club.points >= 0
