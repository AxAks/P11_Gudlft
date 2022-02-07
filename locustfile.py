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
        self.client.post("/show_summary", 'test@club.com')
        #self.client.get("/book/<competition_name>/<club_name>", )
        #self.client.post("/purchase_places", )
        self.client.get("/logout")
