import pytest

from config import COURIER_REGISTER_USER_EXIST_403, COURIER_REGISTER_MISSING_DATA_403
from helpers import generate_new_user_data
from methods.user_methods import UserMethods
from tests.user.login.fx_login_user import fx_login_user


class TestLoginUser:

    def test_login_user(self, fx_login_user):

        user = fx_login_user

        payload = user

        # логиним пользователя
        r_login = UserMethods().login_user(payload)

        assert r_login.status_code == 200 and r_login.json()["success"] == True, f"Ошибка авторизации пользователя"


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

        assert r_register.status_code == 403 and r_register.json()["message"] == COURIER_REGISTER_USER_EXIST_403
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

        assert r_register.status_code == 403 and r_register.json()["message"] == COURIER_REGISTER_MISSING_DATA_403
        print(r_register.json()["message"])



