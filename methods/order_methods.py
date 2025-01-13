import secrets

import requests
from config import BASE_URL

class OrderMethods:

    # создание заказа
    def create_order(self, payload):

        # Создание заказа
        r_order = requests.post(f'{BASE_URL}orders', data=payload)
        return r_order

    # получение id ингредиентов
    def get_ingredients(self):
        r_ingredients = requests.get(f'{BASE_URL}ingredients')
        ingredients = r_ingredients.json()

        # Извлекаем все _id ингредиентов
        ingredients_ids = [item["_id"] for item in ingredients["data"]]

        return ingredients_ids

    # создание несуществующего id ингредиента
    def create_invalid_ingredient_id(self):
        ingredients_ids = OrderMethods().get_ingredients()

        while True:
            invalid_id = secrets.token_hex(24)
            if invalid_id not in ingredients_ids:
                return invalid_id
