"""
Tests file for researches in database
"""
from lib_database.lib_database import get_club_by_email, get_club_by_name, update_competition_places, \
    update_club_points
from models.clubs import Club


def test_load_clubs(test_club_as_list): # test à réécrire
    """
    Checks that the list of clubs can be loaded from a json database file
    """
    assert len(test_club_as_list) == 1


def test_load_competitions(test_competition_as_list): # test à réécrire
    """
    Checks that the list of competitions can be loaded from a json database file
    """
    assert len(test_competition_as_list) == 1


def test_a_registered_email_should_return_a_club(test_club_as_list):
    """
    Checks that a registered email is found
    """
    email = "test@club.com"
    assert isinstance(get_club_by_email(email), Club)


def test_an_unregistered_email_should_return_none(test_club_as_list):
    """
    Checks that an unregistered email cannot be found
    """
    clubs = [club for club in test_club_as_list]
    email = 'unregistered_user@testclub.com'
    assert get_club_by_email(email) is None


def test_a_registered_club_name_should_return_the_matching_club():
    """
    Checks that a registered club name returns the club
    """
    club_name = "Test Club"
    assert isinstance(get_club_by_name(club_name), Club)


def test_an_unregistered_club_name_should_return_none(test_club_as_list):
    """
    Checks that an unregistered club name cannot be found
    """
    club_name = 'I am not a Club'
    assert get_club_by_email(club_name) is None


def test_update_competition_places(test_competition_as_obj, test_new_competition_places):  # test à écrire
    updated_competition = update_competition_places(test_competition_as_obj, test_new_competition_places)
    assert updated_competition.number_of_places >= 0


def test_update_club_points(test_db_club, test_new_club_points, mocker_test_db_club, ):  # test à écrire
    updated_club = update_club_points(test_db_club, test_new_club_points)
    assert updated_club.number_of_places >= 0
