import pytest
import allure
from generators import generate_random_string, register_new_courier_and_return_login_password
from methods.courier_methods import CourierMethods


@allure.epic("API Яндекс.Самокат")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        response = CourierMethods.create_courier(login, password, first_name)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        CourierMethods.delete_courier(login, password)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        create_response = CourierMethods.create_courier(login, password, first_name)
        assert create_response.status_code == 201

        duplicate_response = CourierMethods.create_courier(login, "different_password", "different_name")

        assert duplicate_response.status_code == 409
        assert duplicate_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

        CourierMethods.delete_courier(login, password)

    @allure.title("Ошибка при создании курьера без логина")
    def test_create_courier_without_login_fails(self):
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        response = CourierMethods.create_courier("", password, first_name)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Ошибка при создании курьера без пароля")
    def test_create_courier_without_password_fails(self):
        login = generate_random_string(10)
        first_name = generate_random_string(10)

        response = CourierMethods.create_courier(login, "", first_name)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Ошибка при создании курьера без имени")
    def test_create_courier_without_first_name_fails(self):
        login = generate_random_string(10)
        password = generate_random_string(10)

        response = CourierMethods.create_courier(login, password, "")

        assert response.status_code == 400
        assert "message" in response.json() ## БАГ API: ожидается 400, но возвращается 201

    @allure.title("Проверка всех обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_required_field(self, missing_field):
        data = {
            "login": generate_random_string(10) if missing_field != "login" else "",
            "password": generate_random_string(10) if missing_field != "password" else "",
            "firstName": generate_random_string(10) if missing_field != "firstName" else ""
        }

        response = CourierMethods.create_courier(
            data["login"],
            data["password"],
            data["firstName"]
        )

        assert response.status_code == 400
        assert "message" in response.json() # БАГ API: ожидается 400, но возвращается 201 из-за firstName


    @allure.title("Создание курьера с существующим логином возвращает ошибку")
    def test_create_courier_existing_login(self):
        login = generate_random_string(10)
        password1 = generate_random_string(10)
        first_name1 = generate_random_string(10)

        response1 = CourierMethods.create_courier(login, password1, first_name1)
        assert response1.status_code == 201

        password2 = generate_random_string(10)
        first_name2 = generate_random_string(10)

        response2 = CourierMethods.create_courier(login, password2, first_name2)

        assert response2.status_code == 409
        assert "уже используется" in response2.json()["message"]

        CourierMethods.delete_courier(login, password1)