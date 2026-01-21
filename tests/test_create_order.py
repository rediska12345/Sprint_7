import pytest
import allure
from data import *
from methods.order_methods import OrderMethods

@allure.epic("API Яндекс.Самокат")
@allure.feature("Создание заказа")
class TestCreateOrder:
    
    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        response = OrderMethods.create_order(ORDER_WITHOUT_COLOR)
        
        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] > 0
    
    @allure.title("Создание заказа с цветом BLACK")
    def test_create_order_black_color(self):
        response = OrderMethods.create_order(ORDER_BLACK_COLOR)
        
        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] > 0
    
    @allure.title("Создание заказа с цветом GREY")
    def test_create_order_grey_color(self):
        response = OrderMethods.create_order(ORDER_GREY_COLOR)
        
        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] > 0
    
    @allure.title("Создание заказа с цветами BLACK и GREY")
    def test_create_order_both_colors(self):
        response = OrderMethods.create_order(ORDER_BOTH_COLORS)
        
        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] > 0
