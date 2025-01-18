import pytest
from helpers import generate_new_user_data
from methods.user_methods import UserMethods


@pytest.fixture
def fx_update_user(request):

    print("\n* Начало теста.")
    print("* Генерируем данные для регистрации пользователя.")
    user_data = generate_new_user_data()

    print("* Регистрируем пользователя.")
    r_register = UserMethods().register_user(user_data)
    user_data = {
        "email": user_data['email'],
        "password": user_data['password'],
        "name" : user_data['name'],
        "access_token" : r_register.json()["accessToken"]
    }

    # передаем набор данных по параметру в тест
    yield user_data

    # Получаем токен из request.node после выполнения теста
    access_token = user_data["access_token"]
    if user_data["access_token"]:
        print(f"* Удаляем пользователя с access_token: {access_token[:20]}***")
        UserMethods().delete_user(user_data, access_token)
        print(f"* Пользователь удален.")
    else:
        print("* Токен не был найден, пользователь не удален.")

    print("* Конец теста.\n")




