"""
Tests file for request info extractions
"""
from lib_request.lib_request import extract_club_email, extract_required_places


def test_no_email_should_not_be_accepted(): # ??
    """
    Checks that an error email is not registered
    """
    assert True is False
    pass
    assert extract_club_email('request_mock') not in ['', None]  # a revoir !! fixture pour les requests


def test_amount_of_places_should_be_an_int():
    """
    Checks that the input can be converted into an integer
    """
    amount = 'a'
    assert type(extract_required_places(amount)) == int

