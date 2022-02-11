"""
File for Unit Tests in route show_summary
"""
from libs.lib_show_summary import extract_club_email, is_email_blank, get_club_by_email


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


def test_a_blank_email_should_return_true():
    """
    Checks that A empty text field returns True
    """
    email = ""
    assert is_email_blank(email) is True


def test_a_blank_email_should_return_false(test_club):
    """
    Checks that a fulfilled text field returns False
    """
    email = test_club['email']
    assert is_email_blank(email) is False


def test_a_registered_email_should_return_a_club(test_club_as_list, test_club):
    """
    Checks that a registered email is found if existing
    """
    email = test_club['email']
    assert get_club_by_email(email, test_club_as_list) == test_club


def test_an_unregistered_email_should_return_none(test_club_as_list):
    """
    Checks that an unregistered email cannot be found
    """
    clubs = [club for club in test_club_as_list]
    email = 'unregistered_user@testclub.com'
    assert get_club_by_email(email, clubs) is None
