"""
Lib for functions related to the purchase_places route
"""
from typing import Dict, Union


def extract_club_name(form: Dict) -> str:
    """
    Enables to get the name of a club from the request
    """
    return form['club_name']


def extract_competition_name(form: Dict) -> str:
    """
    Enables to get the name of a competition from a request
    """
    return form['competition_name']


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


def check_competition_places(places_required_as_int, total_places_as_int):
    """
    Compares the requested amount of places for a competition
    with the available amount of places remaining
    """
    return total_places_as_int - places_required_as_int >= 0


def calculate_required_points(places_required_as_int):
    """
    Calculates the ratio points/place
    """
    return 3 * int(places_required_as_int)


def check_club_points(needed_amount_of_points, total_points_as_int):
    """
    Compares the requested amount of places for a competition
    with the number of points the club has
    """
    return total_points_as_int - needed_amount_of_points >= 0


def check_required_places_amount(places_required_as_int, limit=12):
    """
    Checks if the amount of places desired is below the max limit allowed
    """
    return limit - places_required_as_int >= 0


def check_booking_possible(has_enough_places, has_enough_points,
                           competition_is_in_the_future, places_required_is_below_limit):
    """
    Checks if the booking of a competition made by a club is possible
    """
    return has_enough_places and has_enough_points and competition_is_in_the_future and places_required_is_below_limit


def book_places(club: Dict, competition: Dict,
                places_required_as_int: int, total_places_as_int: int,
                needed_amount_of_points: int, total_points_as_int: int) -> tuple[dict, dict]:

    updated_club_points = total_points_as_int - needed_amount_of_points
    club['points'] = str(updated_club_points)
    updated_competition_places = total_places_as_int - places_required_as_int
    competition['number_of_places'] = str(updated_competition_places)
    return club, competition


def update_and_get_obj_attribute_for_db(database, category, obj, attribute) -> Union[str, None]:  # pas de test de rédigé !
    for obj_in_db in database[category]:
        if obj_in_db['name'] == obj['name']:
            try:
                obj_in_db[attribute] = str(obj[attribute])
            except Exception as e:
                raise Exception(e)
            return obj_in_db[attribute]
