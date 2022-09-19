from locust import HttpUser, task, between
from random import randint


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_foods(self):
        collection_id = randint(2, 6)
        self.client.get(
            f'/store/foods/?collection_id={collection_id}',
            name='/store/foods')

    @task(4)
    def view_food(self):
        food_id = randint(1, 1000)
        self.client.get(
            f'/store/foods/{food_id}',
            name='/store/foods/:id')

    @task(1)
    def add_to_cart(self):
        foodid = randint(1, 10)
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name='/store/carts/items',
            json={'food_id': food_id, 'quantity': 1}
        )

    @task
    def say_hello(self):
        self.client.get('/playground/hello/')

    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']
