import pytest


@pytest.fixture
def fx_all_orders(request) -> dict:

    print("\n* Начало теста.")

    yield

    print("* Конец теста.\n")







