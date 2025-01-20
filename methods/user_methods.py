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
            "Authorization": access_token
        }

        payload = {
                "email": user_data.get("email"),
                "password": user_data.get("password")
        }

        r_delete = requests.post(f'{BASE_URL}auth/user', json=payload, headers=headers)
        return r_delete


    def get_user_data(self, headers=None):

        r_user = requests.get(f'{BASE_URL}auth/user', headers=headers)
        return r_user


    def update_user(self, payload: json, headers=None):

        self.get_user_data(headers=headers)
        r_update = requests.patch(f'{BASE_URL}auth/user', json=payload, headers=headers)
        return r_update

