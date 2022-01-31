from locust import HttpUser, task
import server


class HelloWorldUser(HttpUser):
    @task
    def index(self):
        self.client = server.app.client()
        self.client.get("/")

"""
class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
"""