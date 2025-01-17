import pytest
from config import LOGIN_USER_MISSING_DATA_401
from methods.user_methods import UserMethods
from tests.user.login.fx_login_user import fx_login_user


class TestLoginUser:

    @pytest.mark.parametrize("valid_data", ["valid_user"])
    def test_login_user_with_valid_data(self, fx_login_user, valid_data, request):

        user_data = fx_login_user[valid_data]
        print(f"* Пользователь - {user_data}")

        # логиним пользователя
        r_login = UserMethods().login_user(user_data)

        print("* Проверка результатов.")
        assert r_login.status_code == 200 and r_login.json()["accessToken"] is not None, f"Ошибка авторизации пользователя"

        # Установка атрибута access_token в request.node
        request.node.access_token = r_login.json()["accessToken"]


    @pytest.mark.parametrize(
        "invalid_data",
        [
            "invalid_email",
            "invalid_password"
        ]
    )
    def test_login_with_incorrect_data(self, fx_login_user, invalid_data, request):

        user_data = fx_login_user[invalid_data]
        print(f"* Пользователь - {user_data}")

        # логиним пользователя
        r_login = UserMethods().login_user(user_data)

        print("* Проверка результатов.")
        assert r_login.status_code == 401 and r_login.json()["message"] == LOGIN_USER_MISSING_DATA_401
        print(f"* Response body message: {r_login.json()['message']}")



