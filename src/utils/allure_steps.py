import allure
from typing import Dict, Any, List


class PetStoreSteps:
    """Allure шаги для PetStore API"""
    
    @staticmethod
    @allure.step("Добавить питомца")
    def add_pet(api_client, pet_data: Dict[str, Any]):
        return api_client.add_pet(pet_data)
    
    @staticmethod
    @allure.step("Получить питомца по ID: {pet_id}")
    def get_pet(api_client, pet_id: int):
        return api_client.get_pet(pet_id)
    
    @staticmethod
    @allure.step("Обновить питомца")
    def update_pet(api_client, pet_data: Dict[str, Any]):
        return api_client.update_pet(pet_data)
    
    @staticmethod
    @allure.step("Удалить питомца по ID: {pet_id}")
    def delete_pet(api_client, pet_id: int):
        return api_client.delete_pet(pet_id)
    
    @staticmethod
    @allure.step("Найти питомцев по статусу: {status}")
    def find_pets_by_status(api_client, status: str):
        return api_client.find_pets_by_status(status)
    
    @staticmethod
    @allure.step("Обновить питомца через форму (ID: {pet_id}, имя: {name}, статус: {status})")
    def update_pet_with_form(api_client, pet_id: int, name: str = None, status: str = None):
        return api_client.update_pet_with_form(pet_id, name, status)
    
    @staticmethod
    @allure.step("Получить инвентарь магазина")
    def get_inventory(api_client):
        return api_client.get_inventory()
    
    @staticmethod
    @allure.step("Разместить заказ")
    def place_order(api_client, order_data: Dict[str, Any]):
        return api_client.place_order(order_data)
    
    @staticmethod
    @allure.step("Получить заказ по ID: {order_id}")
    def get_order(api_client, order_id: int):
        return api_client.get_order(order_id)
    
    @staticmethod
    @allure.step("Удалить заказ по ID: {order_id}")
    def delete_order(api_client, order_id: int):
        return api_client.delete_order(order_id)
    
    @staticmethod
    @allure.step("Создать пользователя")
    def create_user(api_client, user_data: Dict[str, Any]):
        return api_client.create_user(user_data)
    
    @staticmethod
    @allure.step("Получить пользователя по имени: {username}")
    def get_user(api_client, username: str):
        return api_client.get_user(username)
    
    @staticmethod
    @allure.step("Обновить пользователя: {username}")
    def update_user(api_client, username: str, user_data: Dict[str, Any]):
        return api_client.update_user(username, user_data)
    
    @staticmethod
    @allure.step("Удалить пользователя: {username}")
    def delete_user(api_client, username: str):
        return api_client.delete_user(username)
    
    @staticmethod
    @allure.step("Создать пользователей из списка")
    def create_users_with_list(api_client, users_data: List[Dict[str, Any]]):
        return api_client.create_users_with_list(users_data)
    
    @staticmethod
    @allure.step("Создать пользователей из массива")
    def create_users_with_array(api_client, users_data: List[Dict[str, Any]]):
        return api_client.create_users_with_array(users_data)
    
    @staticmethod
    @allure.step("Логин пользователя: {username}")
    def user_login(api_client, username: str, password: str):
        return api_client.user_login(username, password)
    
    @staticmethod
    @allure.step("Логаут пользователя")
    def user_logout(api_client):
        return api_client.user_logout()


class ValidationSteps:
    """Allure шаги для валидации"""
    
    @staticmethod
    @allure.step("Проверить статус код: {expected_status}")
    def validate_status_code(response, expected_status: int):
        assert response.status_code == expected_status, \
            f"Expected status {expected_status}, but got {response.status_code}"
    
    @staticmethod
    @allure.step("Проверить что ответ содержит поле: {field}")
    def validate_response_contains_field(response_data, field: str):
        assert field in response_data, f"Response doesn't contain field: {field}"
    
    @staticmethod
    @allure.step("Проверить значение поля: {field} = {expected_value}")
    def validate_field_value(response_data, field: str, expected_value):
        assert response_data[field] == expected_value, \
            f"Field {field} expected to be {expected_value}, but got {response_data[field]}"
    
    @staticmethod
    @allure.step("Проверить что ответ является списком")
    def validate_response_is_list(response_data):
        assert isinstance(response_data, list), "Response should be a list"
    
    @staticmethod
    @allure.step("Проверить что ответ является словарем")
    def validate_response_is_dict(response_data):
        assert isinstance(response_data, dict), "Response should be a dictionary"
    
    @staticmethod
    @allure.step("Проверить что список не пустой")
    def validate_list_not_empty(response_data):
        assert len(response_data) > 0, "List should not be empty"