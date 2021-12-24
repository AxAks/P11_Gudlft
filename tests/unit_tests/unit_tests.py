"""
File for Unit Tests :

TDD approach :
1 🔴  Red : write a unit test that fails.
2 ✅  Green : write the source code that makes the test pass.
3 🛠  Refactor : refactor the source code to improve it.
"""

import pytest
import config
from server import find_club, extract_email_from_request


@pytest.fixture   # simulation de client pour les requests, à revoir ...
def client():
    tested_app = config.app
    test_db = 'tests/db_for_tests.json'
    with tested_app.test_client() as client:
        with tested_app.app_context():
            config.load_database(test_db)
        yield client


def test_load_clubs():
    """
    Checks that the list of clubs can be loaded from a json database file
    """
    list_of_clubs = config.load_database('tests/db_for_tests.json')['clubs']  # test pas tres pertinent, à revoir
    assert list_of_clubs is not None


def test_load_competitions(client): # test pas tres pertinent, à revoir
    """
    Checks that the list of competitions can be loaded from a json database file
    """
    competitions = config.load_database('tests/db_for_tests.json')['competitions']
    assert competitions is not None


def test_index():
    """

    """
    pass


def test_show_summary_registered_user():
    """
    Checks that a registered email is found
    """
    # si l'adresse est dans la base : OK
    # si l'adresse n'est pas dans la base : NOK

    email = "john@simplylift.co"
    assert find_club(email) is not None


def test_show_summary_unregistered_user():
    """
    Checks that an unregistered email cannot not found
    """

    email = 'unregistered_user@testclub.com'
    assert find_club(email) is None


def test_show_summary_malformed_email_address():
    """

    """
    email = 'malformed_address@testclub.co'
    pass


def test_show_summary_no_email_given():
    """
    Checks that an error email is not registered
    """
    assert extract_email_from_request() not in ['', None] # a revoir !!


def test_book():
    """
    TDD : When a place for a competition is bought, the number of points is deduced
    """
    pass


def test_purchase_places():
    """

    """
    pass


def test_display_points():
    """

    """
    pass


def test_logout():
    """

    """
    pass
