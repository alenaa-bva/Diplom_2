
from config import GET_ORDERS_JWT_EXPIRED_403, EXPIRED_TOKEN
from methods.order_methods import OrderMethods
from tests.order.get.fx_get_order import fx_get_order


class TestGetOrder:

    def test_get_empty_list_of_user_orders(self, fx_get_order):

        user_data = fx_get_order
        print(f"* Пользователь - {user_data}")

        # добавляем accessToken в хедеры
        headers = {
            "Authorization": user_data["access_token"]
        }

        print("* Получаем заказы пользователя.")
        r_order = OrderMethods().get_user_orders(headers)

        print("* Проверка результатов.")
        assert r_order.status_code == 200 and r_order.json()["orders"] == [], f"Ошибка получения списка заказов"


    def test_get_list_of_user_orders(self, fx_get_order):

        payload = {'ingredients':
                       []
                   }

        user_data = fx_get_order
        print(f"* Пользователь - {user_data}")

        # добавляем accessToken в хедеры
        headers = {
            "Authorization": user_data["access_token"]
        }

        # получаем список из id ингредиентов
        ingredients_ids = OrderMethods().get_ingredients()
        payload['ingredients'] = ingredients_ids

        print("* Создаем заказ авторизованным пользователем.")
        OrderMethods().create_order(payload, headers)

        print("* Получаем заказы пользователя.")
        r_order_get = OrderMethods().get_user_orders(headers)

        print("* Проверка результатов.")
        assert r_order_get.status_code == 200 and len(r_order_get.json()["orders"]) == 1, f"Ошибка получения списка заказов"


    def test_get_orders_unauthorized_user(self):

        print("\n* Начало теста.")

        # добавляем рандомный access_token в хедеры
        headers = {
            "Authorization" : EXPIRED_TOKEN

        }

        print("* Получаем заказы пользователя.")
        r_order = OrderMethods().get_user_orders(headers)

        print("* Проверка результатов.")
        assert r_order.status_code == 403 and r_order.json()["message"] == GET_ORDERS_JWT_EXPIRED_403, f"Ошибка получения списка заказов"
        print(f"* Response body message: {r_order.json()['message']}")
        print("* Конец теста.\n")


    def test_get_orders(self):

        print("\n* Начало теста.")

        print("* Получаем все заказы.")
        r_order = OrderMethods().get_all_orders()

        print("* Проверка результатов.")
        assert r_order.status_code == 200 and len(r_order.json()["orders"]) > 0, f"Ошибка получения списка заказов"
        print("* Конец теста.\n")



