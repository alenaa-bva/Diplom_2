import requests
import random
import string

from config import BASE_URL


def register_new_user():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    user_data = {
        "email": "",
        "password": "",
        "name": "",
        "accessToken": ""
    }

    # генерируем данные пользователя
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{BASE_URL}auth/register', data=payload)

    # забираем accessToken
    accessToken = response.json()["accessToken"]

    # если регистрация прошла успешно (код ответа 200), добавляем в список данные пользователя и accessToken
    if response.status_code == 200:
        user_data["email"] = email
        user_data["password"] = password
        user_data["name"] = name
        user_data["accessToken"] = accessToken

    # возвращаем список
    return user_data

def generate_new_user_data():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    user_data = []

    # генерируем данные пользователя
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    user_data.append(email)
    user_data.append(password)
    user_data.append(name)

    # возвращаем список
    return user_data

def delete_user(self):
    user_data = register_new_user()

    headers = {
        "Authorization": user_data.get("accessToken"),
        "Content-Type": "application/json"
    }

    payload = {
            "email": user_data.get("email"),
            "password": user_data.get("password")
    }

    r_delete = requests.post(f'{BASE_URL}auth/user', json=payload, headers=headers)
    return r_delete
