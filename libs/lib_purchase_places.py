"""
Lib for functions related to the purchase_places route
"""
from typing import Dict, Union, List, Tuple


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


def extract_requested_places(form: Dict) -> int:
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
    """
    Converts a string-formated number of places from the request to an integer
    Can raise Value Error
    """
    competition_places = int(places)

    if competition_places <= 0:
        raise ValueError()

    return competition_places


def convert_club_points_to_int(points: str) -> int:
    """
    Converts a string-formated number of points from the request to an integer
    Can raise Value Error
    """
    club_points = int(points)

    if club_points <= 0:
        raise ValueError()

    return club_points


def check_competition_places(places_requested_as_int, total_places_as_int):
    """
    Compares the requested amount of places for a competition
    with the available amount of places remaining
    """
    return total_places_as_int - places_requested_as_int >= 0


def calculate_required_points(places_requested_as_int):
    """
    Calculates the ratio points/place
    """
    return 3 * places_requested_as_int


def spot_club_bookings_field_in_registry(bookings_registry: Dict[str, List[Dict[str, int]]],
                                         club: Dict,
                                         competition: Dict) -> Dict:
    """
    extracts the record of already booked places to a competition for a given club from the registry
    can raise a keyError if club or competition does not exist in registry
    """
    club_already_booked_places_per_competition_recap = {}
    found_competition_places_booked_dict = {}

    for club_name in bookings_registry:
        if club['name'] == club_name:
            club_already_booked_places_per_competition_recap[club['name']] = bookings_registry[club['name']]
            break
    if len(club_already_booked_places_per_competition_recap) == 0:
        raise KeyError(f"Error: the club:{club['name']} could not be found")

    for already_booked_places in club_already_booked_places_per_competition_recap[club['name']]:
        extracted_competition_name = list(already_booked_places)[0]
        if competition['name'] == extracted_competition_name:
            found_competition_places_booked_dict = already_booked_places
            break
    if len(found_competition_places_booked_dict) == 0:
        raise KeyError(f"Error: the competition: {competition['name']} could not be found")

    return found_competition_places_booked_dict


def extract_nb_booked_places_for_competition(club_competition_points_booked_dict: Dict, competition: Dict) -> int:
    """
    Returns the amount of places already booked by a club in previous requests
    from the corresponding registry entry
    """
    return club_competition_points_booked_dict[competition['name']]


def calculate_total_desired_places(nb_already_booked_places: int, places_requested_as_int: int) -> int:
    """
    Calculates the sum of requested places to a competition for a club.
    It takes into account the previous purchase orders.
    """
    return nb_already_booked_places + places_requested_as_int


def update_and_get_booked_places_in_registry(bookings_registry: Dict[str, List[Dict[str, int]]],
                                             club: Dict, competition: Dict,
                                             total_desired_nb_places_as_int) -> Dict:
    """
    Inserts the new number of booked places for a couple club/competition into the registry
    """
    competition_points_booked_dict = spot_club_bookings_field_in_registry(bookings_registry, club, competition)
    competition_points_booked_dict[competition['name']] = total_desired_nb_places_as_int
    return competition_points_booked_dict


def check_club_points(needed_amount_of_points: int, total_points_as_int: int) -> bool:
    """
    Compares the requested amount of places for a competition
    with the number of points the club has
    """
    return total_points_as_int - needed_amount_of_points >= 0


def check_required_places_amount(total_desired_nb_places_as_int: int, limit: int = 12) -> bool:
    """
    Checks if the total amount of places desired is below the max limit allowed
    """
    return limit - total_desired_nb_places_as_int >= 0


def check_booking_possible(has_enough_places: bool, has_enough_points: bool,
                           competition_is_in_the_future: bool, places_required_is_below_limit: bool) -> bool:
    """
    Checks if the booking of a competition made by a club is possible
    """
    return has_enough_places and has_enough_points and competition_is_in_the_future and places_required_is_below_limit


def book_places(club: Dict, competition: Dict,
                places_requested_as_int: int, total_places_as_int: int,
                needed_amount_of_points: int, total_points_as_int: int) -> Tuple[dict, dict]:
    """
    Updates the competition object with the remaining number of places
    and the club object with the remaining number of points
    """

    updated_club_points = total_points_as_int - needed_amount_of_points
    club['points'] = str(updated_club_points)
    updated_competition_places = total_places_as_int - places_requested_as_int
    competition['number_of_places'] = str(updated_competition_places)
    return club, competition


def update_and_get_obj_attribute_for_db(database, category, obj, attribute) -> Union[str, None]:
    """
    prepares the competition and club the objects to be updated in DB
    """
    for obj_in_db in database[category]:
        if obj_in_db['name'] == obj['name']:
            try:
                obj_in_db[attribute] = str(obj[attribute])
            except Exception as e:
                raise Exception(e)
            return obj_in_db[attribute]
