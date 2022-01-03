"""
Tests Conf File for pytest
"""
import pytest

import config
import utils


@pytest.fixture()  # simulation de client pour les requests, à revoir ...
def client():
    tested_app = config.app
    test_db = 'tests/db_for_tests.json'
    with tested_app.test_client() as client:
        with tested_app.app_context():
            utils.load(test_db)
        yield client()

