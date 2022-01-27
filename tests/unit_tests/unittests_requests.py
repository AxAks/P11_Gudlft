"""
Tests file for request info extractions
"""
import pytest

from lib_request.lib_request import extract_required_places,\
    extract_club_email, extract_competition_name, extract_club_name



def test_an_entered_club_email_should_return_a_string(test_club):
    """
    Checks that the input is a valid string
    """
    form = {'email': test_club['email']}
    assert 'email' in form.keys()
    assert isinstance(extract_club_email(form), str)


def test_an_empty_club_email_should_return_an_empty_string():
    """
    Checks that the input is a valid string
    """
    form = {'email': ''}
    assert 'email' in form.keys()
    assert extract_club_email(form) == ''


def test_an_entered_competition_name_should_return_a_string(test_future_competition):
    """
    Checks that the input is a valid string
    """
    form = {'competition_name': test_future_competition['name']}
    assert 'competition_name' in form.keys()
    assert isinstance(extract_competition_name(form), str)


def test_an_empty_competition_name_should_return_an_empty_string():
    """
    Checks that the input is a valid string
    """
    form = {'competition_name': ''}
    assert 'competition_name' in form.keys()
    assert extract_competition_name(form) == ''


def test_an_entered_club_name_should_return_a_string(test_club):
    """
    Checks that the input is a valid string
    """
    form = {'club_name': test_club['name']}
    assert 'club_name' in form.keys()
    assert isinstance(extract_club_name(form), str)


def test_an_empty_club_name_should_return_an_empty_string():
    """
    Checks that the input is a valid string
    """
    form = {'club_name': ''}
    assert 'club_name' in form.keys()
    assert extract_club_name(form) == ''


def test_an_entered_amount_of_places_should_return_a_int():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': '2'}
    assert 'places' in form.keys()
    assert isinstance(extract_required_places(form), int)


def test_an_empty_amount_of_places_should_raise_a_value_error():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': ''}
    assert 'places' in form.keys()
    with pytest.raises(ValueError):
        extract_required_places(form)


def test_a_negative_amount_of_places_should_raise_a_value_error():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': '0'}
    assert 'places' in form.keys()
    with pytest.raises(ValueError):
        extract_required_places(form)
