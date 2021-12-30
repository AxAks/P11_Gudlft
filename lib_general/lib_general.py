"""
Temp Lib for functions that need to be sorted
"""


def check_club_points(places_required_as_int, total_points_as_int):
    """
    Compares the requested amount of places for a competition
    with the number of points the club has
    """
    return total_points_as_int - places_required_as_int >= 0


def check_competition_places(places_required_as_int, total_places_as_int):
    """
    Compares the requested amount of places for a competition
    with the available amount of places remaining
    """
    return total_places_as_int - places_required_as_int >= 0


def check_booking_possible(has_enough_places, has_enough_points):
    """
    Checks if the booking of a competition made by a club is possible
    """
    return has_enough_places and has_enough_points
