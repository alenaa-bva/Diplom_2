# Создание пользователя:
# создать уникального пользователя; - готов
# создать пользователя, который уже зарегистрирован; - готов
# создать пользователя и не заполнить одно из обязательных полей. - готов
# Логин пользователя:
# логин под существующим пользователем, - готов
# логин с неверным логином и паролем.
# Изменение данных пользователя:
# с авторизацией,
# без авторизации,
# Для обеих ситуаций нужно проверить, что любое поле можно изменить.
# Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
import json

import requests

from config import BASE_URL

class UserMethods:

    def register_user(self, payload: json):

        r_register = requests.post(f'{BASE_URL}auth/register', json=payload)
        return r_register


    def login_user(self, payload: json):
        r_login = requests.post(f'{BASE_URL}auth/login', json=payload)
        return r_login


    def delete_user(self, user_data: dict, access_token: str):

        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        payload = {
                "email": user_data.get("email"),
                "password": user_data.get("password")
        }

        r_delete = requests.post(f'{BASE_URL}auth/user', json=payload, headers=headers)
        return r_delete


    def update_user(self):
        r_update = requests.post(f'{BASE_URL}auth/register', json=payload)
        return r_update

