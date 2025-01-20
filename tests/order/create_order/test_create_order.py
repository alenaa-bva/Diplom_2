from config import ORDER_CREATE_400, EXPIRED_TOKEN, GET_ORDERS_JWT_EXPIRED_403
from methods.order_methods import OrderMethods
from tests.order.create_order.fx_create_order import fx_create_order


class TestCreateOrder:

    def test_create_order_with_authorization(self, fx_create_order):

        print("\n* Начало теста.")

        payload = {'ingredients':
                       []
                   }

        user_data = fx_create_order
        print(f"* Пользователь - {user_data}")

        # добавляем accessToken в хедеры
        headers = {
            "Authorization": user_data["access_token"]
        }

        # получаем список из id ингредиентов
        ingredients_ids = OrderMethods().get_ingredients()
        payload['ingredients'] = ingredients_ids

        print("* Создаем заказ авторизованным пользователем.")
        r_order = OrderMethods().create_order(payload, headers)

        print("* Проверка результатов.")
        assert r_order.status_code == 200 and "_id" in r_order.json()["order"], f"Ошибка создания заказа"


    def test_create_order_unauthorized_user(self):

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


    def test_create_order_orders_expired_token(self):

        print("\n* Начало теста.")

        # добавляем рандомный access_token в хедеры
        headers = {
            "Authorization": EXPIRED_TOKEN
        }

        payload = {'ingredients':
                       []
                   }

        # получаем список из id ингредиентов
        ingredients_ids = OrderMethods().get_ingredients()
        payload['ingredients'] = ingredients_ids

        print("* Создаем заказ пользователю c просроченным токеном.")
        r_order = OrderMethods().create_order(payload, headers)

        print("* Проверка результатов.")
        assert r_order.status_code == 403 and r_order.json()["message"] == GET_ORDERS_JWT_EXPIRED_403, f"Ошибка получения списка заказов"
        print(f"* Response body message: {r_order.json()['message']}")

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