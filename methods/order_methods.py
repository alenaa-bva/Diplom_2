import json
import random
import secrets

import requests
from config import BASE_URL

class OrderMethods:


    def create_order(self, payload: json, headers = None):

        # Создание заказа
        r_order = requests.post(f'{BASE_URL}orders', data=payload, headers = headers)
        return r_order


    # получение id случайных ингредиентов в заданном количестве
    def get_ingredients(self):
        r_ingredients = requests.get(f'{BASE_URL}ingredients')
        ingredients = r_ingredients.json()

        # Извлекаем все _id ингредиентов
        ingredients_ids = [item["_id"] for item in ingredients["data"]]
        count = random.randint(1, len(ingredients_ids))
        random_ingredients_ids = random.sample(ingredients_ids, count)

        return random_ingredients_ids


    # создание несуществующего id ингредиента
    def create_invalid_ingredient_id(self):
        ingredients_ids = self.get_ingredients()

        while True:
            invalid_id = secrets.token_hex(24)
            if invalid_id not in ingredients_ids:
                return invalid_id


    def get_all_orders(self):

        r_orders = requests.get(f'{BASE_URL}orders/all')
        return r_orders


    def get_user_orders(self, headers = None):

        r_orders = requests.get(f'{BASE_URL}orders', headers=headers)

        return r_orders

