"""
Tests Conf File for pytest
"""
import pytest
from flask import Flask

import utils


@pytest.fixture  # simulation de client pour les requests, à revoir ...
def client():
    tested_app = Flask(__name__)
    test_db = 'tests/db_for_tests.json'
    with tested_app.test_client() as client:
        with tested_app.app_context():
            utils.load(test_db)
        yield client
