from locust import HttpUser, task

from server import app, db_path, database, competitions, clubs, bookings_registry

from libs.lib_commons import check_competition_date, get_club_by_name, get_competition_by_name
from libs.lib_purchase_places import extract_club_name, extract_competition_name, extract_requested_places, \
    convert_competition_places_to_int, convert_club_points_to_int, check_competition_places, \
    check_club_points, check_required_places_amount, check_booking_possible, book_places, \
    update_and_get_obj_attribute_for_db, calculate_total_desired_places, calculate_required_points, \
    update_and_get_booked_places_in_registry, spot_club_bookings_field_in_registry, \
    extract_nb_booked_places_for_competition
from libs.lib_show_summary import extract_club_email, is_email_blank, get_club_by_email


class TestUser(HttpUser):
    """
    TestUser inherits from HttpUser to test the app performances with Locust
    """
    @task
    def test_gudlft(self):
        """
         Lists all the website routes to be tested within locust with sample values
        """
        self.client.get("/")
        self.client.post("/show_summary", {"email": "john@simplylift.co"})
        self.client.get("/book/Be The Greatest/Iron Temple", )
        self.client.post("/purchase_places", {"club_name": "Iron Temple",
                                              "competition_name": "Be The Greatest",
                                              "places": "9"})
        self.client.get("/logout")
