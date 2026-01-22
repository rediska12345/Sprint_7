import pytest
import allure
from data import *
from methods.order_methods import OrderMethods

@allure.epic('API Яндекс.Самокат')
@allure.feature('Создание заказа')
class TestCreateOrder:
    
    @pytest.mark.parametrize(
        "order_data, case_name", 
        [
            (ORDER_WITHOUT_COLOR, "без цвета"),
            (ORDER_BLACK_COLOR, "BLACK"),
            (ORDER_GREY_COLOR, "GREY"),
            (ORDER_BOTH_COLORS, "BLACK и GREY")
        ],
        ids=["no_color", "black", "grey", "both_colors"]
    )
    @allure.title('Создание заказа с цветом: {case_name}')
    def test_create_order(self, order_data, case_name):
        response = OrderMethods.create_order(order_data)
        
        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"] > 0
