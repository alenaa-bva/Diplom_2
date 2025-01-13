import requests
import random
import string

from config import BASE_URL


def register_new_user():

    def generate_random_string(length):
        random_string = ''.join(random.choices((string.ascii_letters + string.digits)) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    user_data = []

    # генерируем данные пользователя
    email = f"{generate_random_string(10)}@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": email,
        "password": password,
        "firstName": name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{BASE_URL}auth/register', data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список данные пользователя
    if response.status_code == 200:
        user_data.append(email)
        user_data.append(password)
        user_data.append(name)
    # возвращаем список
    return user_data

def generate_new_user_data():

    def generate_random_string(length):
        random_string = ''.join(random.choices((string.ascii_letters + string.digits)) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    user_data = []

    # генерируем данные пользователя
    email = f"{generate_random_string(10)}@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    user_data.append(email)
    user_data.append(password)
    user_data.append(name)

    # возвращаем список
    return user_data

