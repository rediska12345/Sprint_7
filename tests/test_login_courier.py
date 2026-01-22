import pytest
import allure
from generators import register_new_courier_and_return_login_password
from methods.courier_methods import CourierMethods


@allure.epic("API Яндекс.Самокат")
@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self, courier):
        login, password = courier
        response = CourierMethods.login_courier(login, password)

        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] > 0

    @allure.title("Ошибка при введении логина с неверным логином")
    def test_login_wrong_login(self, courier):
        _, password = courier
        response = CourierMethods.login_courier("wrong_login", password)

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Ошибка при введении логина с неверным паролем")
    def test_login_wrong_password(self, courier):
        login, _ = courier
        response = CourierMethods.login_courier(login, "wrong_password")

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Ошибка при введении логина без логина")
    def test_login_without_login(self, courier):
        _, password = courier
        response = CourierMethods.login_courier("", password)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Логин несуществующего пользователя")
    def test_login_nonexistent_user(self):
        response = CourierMethods.login_courier("nonexistent_user", "any_password")

        assert response.status_code == 404
        assert "message" in response.json()