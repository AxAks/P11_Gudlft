"""
lib for info extraction from requests
"""
from typing import Dict


def extract_club_email(form: Dict) -> str:
    """
    Enables to get the entered email from the request
    """
    return form['email']


def extract_competition_name(form: Dict) -> str:
    """
    Enables to get the name of a competition from a request
    """
    return form['competition_name']


def extract_club_name(form: Dict) -> str:
    """
    Enables to get the name of a club from the request
    """
    return form['club_name']


def extract_required_places(form: Dict) -> int:
    """
    Enables to get from the request the requested amount places to purchase for a competition
    While purchasing
    can raise a ValueError
    """
    places_as_int = int(form['places'])

    if places_as_int < 1:
        raise ValueError('Please provide a positive number of places')

    return places_as_int
