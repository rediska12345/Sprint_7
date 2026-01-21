Финальный проект  7 спринта
Студент: Бритвина Надежда
Когорта: #36
# Автотесты API Яндекс.Самокат

Проект содержит автотесты для API сервиса Яндекс.Самокат (https://qa-scooter.praktikum-services.ru/docs/).

## Структура проекта
- `methods/` - методы для работы с API
- `tests/` - тесты
- `generator.py` - генераторы тестовых данных
- `url.py` - URL endpoints
- `conftest.py` - фикстуры pytest
- `data.py` - данные для заполнения
- `requirements.txt` - зависимости

### Запуск всех тестов
pytest

#### Запуск с генерацией Allure отчета
pytest --alluredir=allure-results

##### Просмотр Allure отчета
allure serve allure_results