"""
File for Unit Tests :

TDD approach :
1 🔴  Red : write a unit test that fails.
2 ✅  Green : write the source code that makes the test pass.
3 🛠  Refactor : refactor the source code to improve it.
"""
from flask import url_for
from werkzeug.utils import redirect

from server import logout

from tests.conftest import client
from unittest_database import *  # à modifier
from unittest_requests import *  # à modifier
from unittest_purchase_places import *  # à modifier

"""
Extraire chaque tests dans un fichier nommé séparé, au fur et a mesure
"""


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


def test_logout(): # le test ne fonctionne pas, mal ecrit ! pb test_client config!
    """
    The logout function should redirect to the homepage
    """
    assert logout() == redirect(url_for('index'))

