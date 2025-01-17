import random
import string

from config import DOMEN


def generate_new_user_data():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём словарь, чтобы метод мог его вернуть
    user_data = {
            "email": "",
            "password": "",
            "name": ""
        }

    # генерируем данные пользователя
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    user_data["email"] = email
    user_data["password"] = password
    user_data["name"] = name

    random_domen = random.choice(list(DOMEN.keys()))
    user_data["email"] = f'{user_data["email"]}{DOMEN[random_domen]}'

    # возвращаем словарь с данными
    return user_data
