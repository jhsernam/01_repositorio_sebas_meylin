from locust import HttpUser, task, between

class ApiUser(HttpUser):

    @task
    def get_sales(self):
        self.client.get("api/bands")


    @task
    def post_sales(self):
        self.client.post("api/bands", json={"name","genre_id"})
