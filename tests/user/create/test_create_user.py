import pytest

from config import REGISTER_USER_EXIST_403, REGISTER_USER_MISSING_DATA_403
from methods.user_methods import UserMethods
from tests.user.create.fx_create_user import fx_create_user
from tests.order.create import da



class TestCreateUser:

    @pytest.mark.parametrize("valid_data", ["valid_user"])
    def test_register_user_valid_data(self, fx_create_user, valid_data, request):

        user_data = fx_create_user[valid_data]

        # регистрируем пользователя
        r_register = UserMethods().register_user(user_data)
        print(f"* Пользователь - {user_data}")

        # Установка атрибута access_token в request.node
        request.node.access_token = r_register.json()["accessToken"]

        print("* Проверка результатов.")
        assert r_register.status_code == 200 and r_register.json()[
            "accessToken"] is not None, f"Ошибка регистрации пользователя"



    @pytest.mark.parametrize("valid_data", ["valid_user"])
    def test_register_existed_user(self, fx_create_user, valid_data, request):

        user_data = fx_create_user[valid_data]

        # регистрируем пользователя
        r_register1 = UserMethods().register_user(user_data)
        print(f"* Пользователь - {user_data}")

        # Установка атрибута access_token в request.node
        request.node.access_token = r_register1.json()["accessToken"]

        # регистрируем пользователя еще раз
        r_register2 = UserMethods().register_user(user_data)

        print("* Проверка результатов.")
        assert r_register2.status_code == 403 and r_register2.json()["message"] == REGISTER_USER_EXIST_403
        print(f"* Response body message: {r_register2.json()['message']}")


    @pytest.mark.parametrize(
        "missing_data",
        [
            "missing_password",
            "missing_email",
            "missing_name"
        ]
    )
    def test_register_user_missing_data(self, fx_create_user, missing_data):

        user_data = fx_create_user[missing_data]
        print(f"* Данные для регистрации - {user_data}")

        # регистрируем пользователя
        r_register = UserMethods().register_user(user_data)

        print("* Проверка результатов.")
        assert r_register.status_code == 403 and r_register.json()["message"] == REGISTER_USER_MISSING_DATA_403
        print(f"* Response body message: {r_register.json()['message']}")


    @pytest.mark.parametrize(
        "invalid_data",
        [
            "invalid_email"
        ]
    )
    def test_register_user_with_incorrect_email(self, fx_create_user, invalid_data):

        user_data = fx_create_user[invalid_data]
        print(f"* Данные для регистрации - {user_data}")

        # регистрируем пользователя
        r_register = UserMethods().register_user(user_data)

        print("* Проверка результатов.")
        assert r_register.status_code == 500





