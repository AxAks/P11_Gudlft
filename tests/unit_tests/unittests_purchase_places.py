from lib_general.lib_general import check_competition_places, check_club_points, check_booking_possible


def test_enough_places_in_competition_should_return_true():
    places_required_as_int = 6
    total_places_in_competition_as_int = 25
    assert check_competition_places(places_required_as_int, total_places_in_competition_as_int) is True


def test_not_enough_places_in_competition_should_return_false():
    places_required_as_int = 26
    total_places_in_competition_as_int = 25
    assert check_competition_places(places_required_as_int, total_places_in_competition_as_int) is False


def test_enough_points_for_club_should_return_true():
    places_required_as_int = 13
    total_club_points_as_int = 13
    assert check_club_points(places_required_as_int, total_club_points_as_int) is True


def test_not_enough_points_for_club_should_return_false():
    places_required_as_int = 14
    total_club_points_as_int = 13
    assert check_club_points(places_required_as_int, total_club_points_as_int) is False


def test_places_ok_points_ok_should_return_true():
    has_enough_places = True
    has_enough_points = True
    assert check_booking_possible(has_enough_places, has_enough_points) is True


def test_places_ok_points_nok_should_return_false():
    has_enough_places = True
    has_enough_points = False
    assert check_booking_possible(has_enough_places, has_enough_points) is False


def test_places_nok_points_ok_should_return_false():
    has_enough_places = False
    has_enough_points = True
    assert check_booking_possible(has_enough_places, has_enough_points) is False


def test_places_nok_points_nok_should_return_false():
    has_enough_places = False
    has_enough_points = False
    assert check_booking_possible(has_enough_places, has_enough_points) is False