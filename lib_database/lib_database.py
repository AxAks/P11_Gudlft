"""
Lib for functions related to database queries
"""
from typing import Union, Dict

from config import gudlft_database, clubs, competitions


def get_club_by_email(email: str) -> Union[Dict, None]:
    """
    Searches a club whose registered contact email matches the email given as parameter
    """
    for club in clubs:
        if email == club['email']:
            return club


def get_club_by_name(name: str) -> Union[Dict, None]:
    """
    Enables to get a club infos from its name
    """
    for club in clubs:
        if name == club['name']:
            return club


def get_competition_by_name(competition_name: str) -> Union[Dict, None]:
    """
    Enables to get a competition infos from its name
    """
    for competition in competitions:
        if competition_name == competition['name']:
            return competition


def update_competition_places_for_db(competition):
    for competition_in_db in gudlft_database['competitions']:
        if competition_in_db['name'] == competition['name']:
            competition_in_db['number_of_places'] = str(competition['number_of_places'])


def update_club_points_for_db(club):
    for club_in_db in gudlft_database['clubs']:
        if club_in_db['name'] == club['name']:
            club_in_db['points'] = str(club['points'])
