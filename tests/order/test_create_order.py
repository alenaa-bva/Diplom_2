
from config import ORDER_CREATE_400
from methods.order_methods import OrderMethods


class TestCreateOrder:

    def test_create_order_without_authorization(self):

        #получаем id ингредиентов
        ingredients_ids = OrderMethods().get_ingredients()

        # собираем payload
        payload = {'ingredients':
                       [ingredients_ids[0], ingredients_ids[1]]
                   }

        # создаем заказ
        r_order = OrderMethods().create_order(payload)
        assert r_order.status_code == 200 and r_order.json()["order"]["number"] is not None, f"Ошибка создания заказа"


    def test_create_order_without_ingredients(self):

        payload = {'ingredients':
                       []
                   }

        # создаем заказ
        r_order = OrderMethods().create_order(payload)
        assert r_order.status_code == 400 and r_order.json()["message"] == ORDER_CREATE_400


    def test_create_order_with_invalid_ingredient_id(self):

        invalid_ingredient_id = OrderMethods().create_invalid_ingredient_id()
        payload = {'ingredients':
                       [invalid_ingredient_id]
                   }

        # создаем заказ
        r_order = OrderMethods().create_order(payload)
        assert r_order.status_code == 500