"""
Lib for
"""
from typing import Union, Dict

from config import clubs, competitions


def get_club_by_email(email: str) -> Union[Dict, None]:
    """
    Searches a club whose registered contact email matches the email given as parameter
    """
    for club in clubs:
        if email == club['email']:
            return club


def get_competition_by_name(competition_name: str):
    """
    Enables to get a competition infos from its name
    """
    competition = [comp for comp in competitions if comp['name'] == competition_name][0]
    return competition


def get_club_by_name(name: str) -> Union[Dict, None]:
    """
    Enables to get a club infos from its name
    """
    for club in clubs:
        if name == club['name']:
            return club