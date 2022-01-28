"""
Lib for functions related to database queries
"""
from typing import Union, Dict, List


def get_club_by_email(email: str, clubs: List[Dict]) -> Union[Dict, None]:
    """
    Searches a club whose registered contact email matches the email given as parameter
    """
    for club in clubs:
        if email == club['email']:
            return club


def get_club_by_name(name: str, clubs: List[Dict]) -> Union[Dict, None]:
    """
    Enables to get a club infos from its name
    """
    for club in clubs:
        if name == club['name']:
            return club


def get_competition_by_name(competition_name: str, competitions: List[Dict]) -> Union[Dict, None]:
    """
    Enables to get a competition infos from its name
    """
    for competition in competitions:
        if competition_name == competition['name']:
            return competition


def convert_competition_places_to_int(places: str) -> int:
    competition_places = int(places)

    if competition_places <= 0:
        raise ValueError()

    return competition_places


def convert_club_points_to_int(points: str) -> int:
    """
    Can  raise ValueError
    """
    club_points = int(points)

    if club_points <= 0:
        raise ValueError()

    return club_points


def update_and_get_competition_places_for_db(competition, database) -> Union[str, None]:
    for competition_in_db in database['competitions']:
        if competition_in_db['name'] == competition['name']:
            competition_in_db['number_of_places'] = str(competition['number_of_places'])
            return competition_in_db['number_of_places']


def update_and_get_club_points_for_db(club, database) -> Union[str, None]:
    for club_in_db in database['clubs']:
        if club_in_db['name'] == club['name']:
            club_in_db['points'] = str(club['points'])
            return club_in_db['points']


def book_places(club: Dict, competition: Dict,
                places_required_as_int: int, total_places_as_int: int,
                needed_amount_of_points: int, total_points_as_int: int) -> tuple[dict, dict]:

    updated_club_points = total_points_as_int - needed_amount_of_points
    club['points'] = str(updated_club_points)
    updated_competition_places = total_places_as_int - places_required_as_int
    competition['number_of_places'] = str(updated_competition_places)
    return club, competition


def calculate_required_points(places_required_as_int):
    """
    Calculates the ratio points/place
    """
    return 3 * int(places_required_as_int)
