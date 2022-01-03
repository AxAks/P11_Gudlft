"""
Tests file for request info extractions
"""
from tests.conftest import client
from lib_request.lib_request import extract_club_email, extract_required_places


def test_no_email_should_not_be_accepted():  # ??
    """
    Checks that an error email is not registered
    """
    assert extract_club_email(client) not in ['', None]  #  a revoir !! fixture pour les requests


def test_an_entered_amount_of_places_should_return_a_int():  #  ??
    """
    Checks that the input can be converted into an integer
    """
    assert True is False
    places = '6'
    assert type(extract_required_places(places)) == int  #  a revoir !! fixture pour les requests
