import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def ping(self):
        self.client.get("/api/ping")

    @task
    def get_cards(self):
        self.client.get("/api/cards")

    def on_start(self):
        self.client.post("/api/userAuth", auth=('test@gmail.com', 'testing'))