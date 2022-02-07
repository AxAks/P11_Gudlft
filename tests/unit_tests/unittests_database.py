"""
Tests file for researches in database
"""
from typing import Dict

from libs.lib_purchase_places import update_and_get_obj_attribute_for_db
from utils import load
from libs.lib_commons import get_club_by_name, get_competition_by_name


def test_load_database(test_db_path):
    """
    Checks that the list of clubs can be loaded from a json database file
    """
    database = load(test_db_path)
    assert isinstance(database, Dict)
    assert 'clubs' in database.keys()
    assert 'competitions' in database.keys()
    assert database['clubs'][0]['name'] == 'Test Club'
    assert database['competitions'][0]['name'] == 'Test Past Competition'


def test_load_competitions(test_competitions_as_list):
    """
    Checks that the list of competitions can be loaded from a json database file
    """
    assert len(test_competitions_as_list) == 3


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


def test_update_and_get_obj_attribute_for_db_club(test_database, test_club_to_be_saved,):
    """
    Checks that the club points passed as arguments can be updated before being saved in database
    """
    assert update_and_get_obj_attribute_for_db(test_database, 'clubs', test_club_to_be_saved, 'points') == '18'


def test_update_and_get_obj_attribute_for_db_competition(test_database, test_future_competition_to_be_saved):
    """
    Checks that the competition places passed as arguments can be updated before being saved in database
    """
    assert update_and_get_obj_attribute_for_db(test_database,
                                               'competitions',
                                               test_future_competition_to_be_saved,
                                               'number_of_places') == '20'
