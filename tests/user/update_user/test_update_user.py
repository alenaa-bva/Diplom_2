import pytest
from config import UNAUTHORIZED_USER_401, UPDATE_USER_ALREADY_EXISTS_403
from helpers import generate_new_user_data
from methods.user_methods import UserMethods
from tests.user.update_user.data import TestParametersCreator
from tests.user.update_user.fx_update_user import fx_update_user


class TestLoginUser:

    user_names = TestParametersCreator().get_valid_test_names()
    @pytest.mark.parametrize(
        "user_name",
        [
            user_names["name_1"],
            user_names["name_2"],
            user_names["name_3"],
            user_names["name_4"],
            user_names["name_5"]
        ]
    )
    def test_update_user_name(self, fx_update_user, user_name):

        print("\n* Начало теста.")

        user_data = fx_update_user
        print(f"* Пользователь - {user_data}")

        # добавляем accessToken в хедеры
        headers = {
            "Authorization": user_data["access_token"]
        }

        # меняем имя на новое
        payload = {
            "email": user_data["email"],
            "name": user_name
        }
        print(f"* Новое имя пользователя - {payload['name']}")

        r_update_user = UserMethods().update_user(payload=payload, headers = headers)

        print("* Проверка результатов.")
        assert r_update_user.status_code == 200 and r_update_user.json()["user"]["name"] == payload['name'], f"Ошибка получения данных пользователя"


    user_emails = TestParametersCreator().get_valid_test_emails()
    @pytest.mark.parametrize(
        "user_email",
        [
            user_emails["email_1"],
            user_emails["email_2"]
        ]
    )
    def test_update_user_email(self, fx_update_user, user_email):

        print("\n* Начало теста.")

        user_data = fx_update_user
        print(f"* Пользователь - {user_data}")

        # добавляем accessToken в хедеры
        headers = {
            "Authorization": user_data["access_token"]
        }

        # меняем email на новый
        payload = {
            "email": f"{user_email}{user_data['email']}",
            "name": user_data["name"]
        }

        print(f"* Новый email пользователя - {payload['email']}")

        r_update_user = UserMethods().update_user(payload=payload, headers = headers)

        print("* Проверка результатов.")
        assert r_update_user.status_code == 200 and r_update_user.json()["user"]["email"] == payload['email'], f"Ошибка получения данных пользователя"


    def test_update_user_unauthorized(self, fx_update_user):
        print("\n* Начало теста.")

        user_data = fx_update_user
        print(f"* Пользователь - {user_data}")

        payload = {
            "email": user_data['email'],
            "name": user_data["name"]
        }

        print("* Обновляем данные неавторизаванного пользователя.")
        r_update_user = UserMethods().update_user(payload=payload, headers=None)

        print("* Проверка результатов.")
        assert r_update_user.status_code == 401 and r_update_user.json()['message'] == UNAUTHORIZED_USER_401, f"Ошибка получения данных пользователя"
        print(f"* Response body message: {r_update_user.json()['message']}")


    def test_update_user_email_on_already_existed(self, fx_update_user):

        print("\n* Начало теста.")

        user_data = fx_update_user
        print(f"* Пользователь - {user_data}")

        # добавляем accessToken в хедеры
        headers = {
            "Authorization": user_data["access_token"]
        }

        # Регистрируем еще пользователя
        new_user_data = generate_new_user_data()
        UserMethods().register_user(new_user_data)
        new_user_email = new_user_data['email']

        # меняем email на email существующего пользователя
        payload = {
            "email": new_user_email,
            "name": user_data["name"]
        }

        print(f"* Новый email пользователя - {payload['email']}")

        r_update_user = UserMethods().update_user(payload=payload, headers = headers)

        print("* Проверка результатов.")
        assert r_update_user.status_code == 403 and r_update_user.json()['message'] == UPDATE_USER_ALREADY_EXISTS_403, f"Ошибка получения данных пользователя"
        print(f"* Response body message: {r_update_user.json()['message']}")


