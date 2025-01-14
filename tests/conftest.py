=import pytest

from helpers import register_new_courier_and_return_login_password, generate_new_courier_data, generate_new_user_data


@pytest.fixture
def user():
    # Подготовка данных
    print("Создание пользователя.")
    user_data = generate_new_user_data

    # Возвращаем пользователя в тест
    yield user_data

    # Очистка после теста
    user = {
        "login": user_data[0],
        "password": user_data[1],
        ""
    }

    # чтобы удалить пользователя, сначала нужно авторизоваться и получить токен
    response = CourierMethods().login_courier(courier)
    if "id" in response.json():
        print("\nУдаление курьера после теста.")
        CourierMethods().delete_courier(response.json()["id"])


