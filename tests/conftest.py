"""
Tests Conf File for pytest
"""
import pytest
import server
import utils


@pytest.fixture
def app():
    tested_app = server.app
    test_db = 'tests/db_for_tests.json'
    with tested_app.app_context():
        utils.load(test_db)
        yield tested_app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
