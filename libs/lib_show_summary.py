"""
Lib for functions related to the show_summary route
"""
from typing import Dict, List, Union


def extract_club_email(form: Dict) -> str:
    """
    Enables to get the entered email from the request
    """
    return form['email']


def is_email_blank(email):
    """
    Checks an email address has been entered
    """
    return email == ''


def get_club_by_email(email: str, clubs: List[Dict]) -> Union[Dict, None]:
    """
    Searches a club whose registered contact email matches the email given as parameter
    """
    for club in clubs:
        if email == club['email']:
            return club