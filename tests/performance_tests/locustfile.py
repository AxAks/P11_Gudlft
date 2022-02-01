from locust import HttpUser, task


class TestUser(HttpUser):

    @task
    def index(self):
        self.client.get("/")


"""
@task
def show_summary(self):
    self.client.post("/show_summary")


@task
def book(self):
    self.client.get("/book/<competition_name>/<club_name>")

@task
def purchase_places(self):
    self.client.post("/purchase_places")

@task
def logout(self):
    self.client.get("/logout")


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
"""