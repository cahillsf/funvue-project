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

    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    def on_start(self):
        self.client.post("/api/userAuth", auth=('test@gmail.com', 'testing'))