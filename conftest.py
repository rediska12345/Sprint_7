import pytest
import requests
from generators import register_new_courier_and_return_login_password
from url import *
from methods.courier_methods import CourierMethods

@pytest.fixture
def create_courier():
    #Создание нового курьера перед тестом и удаление после.
    courier_data = register_new_courier_and_return_login_password()
    if not courier_data:
        pytest.skip("Не удалось создать курьера")

    login, password, first_name = courier_data

    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # Удаление курьера после теста
    delete_payload = {
        "login": login,
        "password": password
    }
    response = requests.put(DELETE_COURIER, data=delete_payload)