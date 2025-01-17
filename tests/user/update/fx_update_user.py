import random

import pytest

from config import DOMEN
from helpers import generate_new_user_data
from methods.user_methods import UserMethods
from tests.user.login.data import TestParametersCreator


@pytest.fixture
def fx_update_user(request):

    print("\n* Начало теста.")
    print("* Генерируем данные для регистрации пользователя.")
    user_data = generate_new_user_data()

    print("* Регистрируем пользователя.")
    UserMethods().register_user(user_data)
    login_data = {
        "email": user_data['email'],
        "password": user_data['password']
    }

    # логинимся и получаем access_token
    r_login = UserMethods().login_user(login_data)
    login_data["access_token"] = r_login.json()['accessToken']

    # передаем набор данных по параметру в тест
    yield login_data

    # Получаем токен из request.node после выполнения теста
    access_token = login_data["access_token"]
    if login_data["access_token"]:
        print(f"* Удаляем пользователя с access_token: {access_token[:20]}***")
        UserMethods().delete_user(login_data, access_token)
    else:
        print("* Токен не был найден, пользователь не удален.")

    print("* Конец теста.\n")





