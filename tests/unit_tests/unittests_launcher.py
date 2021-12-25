"""
File for Unit Tests :

TDD approach :
1 🔴  Red : write a unit test that fails.
2 ✅  Green : write the source code that makes the test pass.
3 🛠  Refactor : refactor the source code to improve it.
"""

import pytest

import config
import utils

from unittest_database import *
from unittest_requests import *


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
    assert True is False
    pass


def test_book():
    """

    """
    assert True is False
    pass


def test_purchase_places():
    """
    TDD : When a place for a competition is bought, the number of points is deduced
    """


def test_():
    assert True is False
    pass


def test_():
    assert True is False
    pass


def test_display_points():
    """

    """
    assert True is False
    pass


def test_logout():
    """

    """
    assert True is False
    pass
