"""
lib for info extraction from requests
"""
from typing import Dict


def extract_club_email(request):
    """
    Enables to get the entered email from the request
    """
    return request.form['email']


def extract_competition_name(request):
    """
    Enables to get the name of a competition from a request
    """
    return request.form['competition_name']


def extract_club_name(request):
    """
    Enables to get the name of a club from the request
    """
    return request.form['club_name']


def extract_required_places(form: Dict):
    """
    Enables to get from the request the requested amount places to purchase for a competition
    While purchasing
    """
    return int(form['places'])
