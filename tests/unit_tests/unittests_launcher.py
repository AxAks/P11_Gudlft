"""
File for Unit Tests :

TDD approach :
1 🔴  Red : write a unit test that fails.
2 ✅  Green : write the source code that makes the test pass.
3 🛠  Refactor : refactor the source code to improve it.
"""

import pytest

import config, utils

from unittest_database \
    import test_load_clubs, test_load_competitions, \
    test_a_registered_email_should_return_a_club, test_an_unregistered_email_should_return_none, \
    test_an_unregistered_email_should_return_none, test_a_malformed_email_address_should_not_be_accepted

from unittest_requests \
    import test_no_email_should_not_be_accepted


"""
Extraire chaque tests dans un fichier nommé séparé, au fur et a mesure
"""


@pytest.fixture  # simulation de client pour les requests, à revoir ...
def client():
    tested_app = config.app
    test_db = 'tests/db_for_tests.json'
    with tested_app.test_client() as client:
        with tested_app.app_context():
            utils.load_database(test_db)
        yield client


def test_index():
    """

    """
    pass


def test_book():
    """

    """
    pass


def test_purchase_places():
    """
    TDD : When a place for a competition is bought, the number of points is deduced
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
