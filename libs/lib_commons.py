"""
Temp Lib for functions that need to be sorted
"""
from datetime import datetime, timedelta
from typing import List, Dict, Union


def check_competition_date(competition_date, now=datetime.now()):
    """
    Checks that the competition is in the future
    """
    return competition_date - now > timedelta(0)


def get_club_by_name(name: str, clubs: List[Dict]) -> Union[Dict, None]:
    """
    Enables to retrieve a given club in the list of all clubs from its name
    """
    for club in clubs:
        if name == club['name']:
            return club


def get_competition_by_name(competition_name: str, competitions: List[Dict]) -> Union[Dict, None]:
    """
    Enables to get a given competition in the list of all competitions from its name
    """
    for competition in competitions:
        if competition_name == competition['name']:
            return competition
