from locust import HttpUser, task


class TestUser(HttpUser):
    """
    TestUser inherits from HttpUser to test the app performances with Locust
    """
    @task
    def test_gudlft(self):
        """
        Sets all the website routes to be tested within locust
        """
        self.client.get("/")
        self.client.post("/show_summary", {"email": "test@club.com"})
        self.client.get("/book/Test Future Competition/Test Club", )
        self.client.post("/purchase_places", {"club_name": "Test Club",
                                              "competition_name": "Test Future Competition",
                                              "places": "9"})
        self.client.get("/logout")
