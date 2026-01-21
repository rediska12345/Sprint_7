import pytest
import allure
from methods.order_methods import OrderMethods

@allure.epic("API Яндекс.Самокат")
@allure.feature("Список заказов")
class TestListOrders:
    
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = OrderMethods.get_orders_list()
        
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
