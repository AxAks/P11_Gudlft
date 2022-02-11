from locust import HttpUser, task


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
        self.client.get("/book/Fall Classic/Iron Temple", )
        self.client.post("/purchase_places", {"club_name": "Iron Temple",
                                              "competition_name": "Fall Classic",
                                              "places": "9"})
        self.client.get("/logout")
