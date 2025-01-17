import pytest

from config import ORDER_CREATE_400
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from tests.order.create.fx_create_order import fx_create_order


class TestCreateOrder:

    @pytest.mark.parametrize("valid_data", ["valid_user"])
    def test_create_order_with_authorization(self, fx_create_order, valid_data, request):

        print("\n* Начало теста.")

        payload = {'ingredients':
                       []
                   }

        user_data = fx_create_order[valid_data]
        print(f"* Пользователь - {user_data}")

        # логиним пользователя
        r_login = UserMethods().login_user(user_data)

        # Установка атрибута access_token в request.node
        request.node.access_token = r_login.json()["accessToken"]

        # добавляем accessToken в хедеры
        headers = {
            "Authorization": r_login.json()["accessToken"]
        }

        # получаем список из id ингредиентов
        ingredients_ids = OrderMethods().get_ingredients()
        payload['ingredients'] = ingredients_ids

        print("* Создаем заказ авторизованным пользователем.")
        r_order = OrderMethods().create_order(payload, headers)

        print("* Проверка результатов.")
        assert r_order.status_code == 200 and "_id" in r_order.json()["order"], f"Ошибка создания заказа"


    def test_create_order_without_authorization(self):

        print("\n* Начало теста.")

        payload = {'ingredients':
                       []
                   }

        # получаем список из id ингредиентов
        ingredients_ids = OrderMethods().get_ingredients()
        payload['ingredients'] = ingredients_ids

        print("* Создаем заказ неавторизованным пользователем.")
        r_order = OrderMethods().create_order(payload)

        print("* Проверка результатов.")
        assert r_order.status_code == 200 and "_id" not in r_order.json()["order"], f"Ошибка создания заказа"

        print("* Конец теста.\n")


    def test_create_order_without_ingredients(self):

        print("\n* Начало теста.")

        payload = {'ingredients':
                       []
                   }

        print("* Создаем заказ без ингредиентов.")
        r_order = OrderMethods().create_order(payload)

        print("* Проверка результатов.")
        assert r_order.status_code == 400 and r_order.json()["message"] == ORDER_CREATE_400
        print(f"* Response body message: {r_order.json()['message']}")

        print("* Конец теста.\n")


    def test_create_order_with_invalid_ingredient_id(self):

        print("\n* Начало теста.")

        payload = {'ingredients':
                       []
                   }

        invalid_ingredient_id = OrderMethods().create_invalid_ingredient_id()
        payload['ingredients'] = invalid_ingredient_id

        print("* Создаем заказ с невалидным хешем.")
        r_order = OrderMethods().create_order(payload)

        print("* Проверка результатов.")
        assert r_order.status_code == 500

        print("* Конец теста.\n")