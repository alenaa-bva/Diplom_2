import pytest
from methods.user_methods import UserMethods
from helpers import generate_new_user_data
from tests.user.create_user.data import TestParametersCreator


@pytest.fixture
def fx_create_user(request) -> dict:

    print("\n* Начало теста.")
    print("* Генерируем данные для регистрации пользователя.")
    user_data = generate_new_user_data()

    register_data = TestParametersCreator().get_test_params(user_data)

    # передаем набор данных по параметру в тест
    yield register_data

    # Получаем токен из request.node после выполнения теста
    access_token = getattr(request.node, "access_token", None)
    if access_token:
        print(f"* Удаляем пользователя с access_token: {access_token[:20]}***")
        UserMethods().delete_user(register_data, access_token)
        print(f"* Пользователь удален.")
    else:
        print("* Токен не был найден, пользователь не удален.")

    print("* Конец теста.\n")




