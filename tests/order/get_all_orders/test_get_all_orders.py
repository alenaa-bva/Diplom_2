from methods.order_methods import OrderMethods


class TestGetOrder:

    def test_get_orders(self):

        print("\n* Начало теста.")

        print("* Получаем все заказы.")
        r_order = OrderMethods().get_all_orders()

        print("* Проверка результатов.")
        assert r_order.status_code == 200 and len(r_order.json()["orders"]) > 0, f"Ошибка получения списка заказов"
        print("* Конец теста.\n")



