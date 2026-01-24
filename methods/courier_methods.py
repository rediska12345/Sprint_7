import requests
import allure
from url import CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER

class CourierMethods:
    
    @staticmethod
    @allure.step("Создание курьера с данными: {login}, {password}, {first_name}")
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(CREATE_COURIER, data=payload)
    
    @staticmethod
    @allure.step("Логин курьера: {login}'")
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(LOGIN_COURIER, data=payload)
    
    @staticmethod
    @allure.step("Удаление курьера: {login}")
    def delete_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.put(DELETE_COURIER, data=payload)
    
    @staticmethod
    @allure.step("Удаление курьера по ID: {courier_id}")
    def delete_courier_by_id(courier_id):
        return requests.delete(f"{DELETE_COURIER}/{courier_id}")
