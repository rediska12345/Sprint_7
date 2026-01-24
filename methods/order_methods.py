import requests
import allure
from url import CREATE_ORDER, LIST_ORDERS

class OrderMethods:
    
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data):
        return requests.post(CREATE_ORDER, json=order_data)
    
    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders_list():
        return requests.get(LIST_ORDERS)
