import random

import pytest

from config import DOMEN
from methods.user_methods import UserMethods

from helpers import generate_new_user_data


@pytest.fixture
def fx_create_user(request) -> dict[str, str]:

    # Подготовка данных
    print("Создание пользователя.")

    user_data_for_registration = generate_new_user_data()

    random_key = random.choice(list(DOMEN.keys()))

    payload = {
        "email": f"{user_data_for_registration[0]}{DOMEN[random_key]}",
        "password": user_data_for_registration[1],
        "name": user_data_for_registration[2]
    }

    # регистрируем пользователя
    r_register = UserMethods().register_user(payload)

    # получаем токен
    access_token = r_register.json()["accessToken"]

    user_data_for_login = {
        "email": f"{user_data_for_registration[0]}{DOMEN[random_key]}",
        "password": user_data_for_registration[1],
        "name": user_data_for_registration[2],
        "access_token": access_token
    }

    # возвращаем пользователя в тест
    yield user_data_for_login

    # удаление пользователя после теста
    # удаляем пользователя по новому токену, полученному из теста, т.к. старый уже будет использован
    print("Удаление пользователя после теста.")
    new_access_token = request.node.get_closest_marker("new_access_token")
    UserMethods().delete_user(user_data_for_login, new_access_token)




