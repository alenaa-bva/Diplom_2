import pytest

from config import DOMEN, REGISTER_USER_EXIST_403, REGISTER_USER_MISSING_DATA_403
from helpers import generate_new_user_data
from methods.user_methods import UserMethods


class TestCreateUser:

    @pytest.mark.parametrize('domen', [
        DOMEN.get("yandex.ru"),
        DOMEN.get("google.com")
    ])
    def test_register_user(self, domen):

        # генерируем данные пользователя
        user_data = generate_new_user_data()

        payload = {
            "email": f"{user_data[0]}{domen}",
            "password": user_data[1],
            "name": user_data[2]
        }

        payload = {
            "email": f"{user_data[0]}{domen}",
            "password": user_data[1],
            "name": user_data[2]
        }

        # регистрируем пользователя
        r_register = UserMethods().register_user(payload)

        assert r_register.status_code == 200 and r_register.json()["success"] == True, f"Ошибка регистрации пользователя"

        # получаем токен
        access_token = r_register.json()["accessToken"]

        # подчищаем данные после теста - удаляем пользователя
        UserMethods().delete_user(payload, access_token)

        # регистрируем пользователя
        r_register = UserMethods().register_user(payload)

        assert r_register.status_code == 200 and r_register.json()["success"] == True, f"Ошибка регистрации пользователя"

        # получаем токен
        access_token = r_register.json()["accessToken"]

        # подчищаем данные после теста - удаляем пользователя
        UserMethods().delete_user(payload, access_token)


    def test_register_existed_user(self):

        # генерируем данные пользователя
        user_data = generate_new_user_data()

        payload = {
            "email": f"{user_data[0]}@yandex.ru",
            "password": user_data[1],
            "name": user_data[2]
        }

        # регистрируем пользователя
        r_register = UserMethods().register_user(payload)

        # получаем токен
        access_token = r_register.json()["accessToken"]

        # регистрируем пользователя еще раз
        r_register = UserMethods().register_user(payload)

        assert r_register.status_code == 403 and r_register.json()["message"] == REGISTER_USER_EXIST_403
        print(r_register.json()["message"])

        # подчищаем данные после теста - удаляем пользователя
        UserMethods().delete_user(payload, access_token)


    @pytest.mark.parametrize('email, password, name', [
        ('', 'password', 'user'),
        ('some_email@yandex.ru', '', 'user'),
        ('some_email@yandex.ru', 'password', '')
    ])
    def test_register_user_without_required_fields(self, email, password, name):

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        # регистрируем пользователя без обязательных полей
        r_register = UserMethods().register_user(payload)

        assert r_register.status_code == 403 and r_register.json()["message"] == REGISTER_USER_MISSING_DATA_403
        print(r_register.json()["message"])



