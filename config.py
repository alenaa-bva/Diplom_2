BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'

ORDER_CREATE_400 = "Ingredient ids must be provided"
REGISTER_USER_EXIST_403 = "User already exists"
REGISTER_USER_MISSING_DATA_403 = "Email, password and name are required fields"
LOGIN_USER_MISSING_DATA_401 = "email or password are incorrect"
GET_ORDERS_JWT_EXPIRED_403 = "jwt expired"

DOMEN = {
    "yandex.ru" : "@yandex.ru",
    "google.com" : "@google.com"
}

EXPIRED_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ODZlYzgzOWVkMjgwMDAxYjU0Y2M1YiIsImlhdCI6MTczNzExNzQzMSwiZXhwIjoxNzM3MTE4NjMxfQ.k3W2Bfm4foubjLI9ug-MUWcXPIGxe42bbV0mIiJEOxM"