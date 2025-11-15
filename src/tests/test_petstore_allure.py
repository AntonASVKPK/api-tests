"""
Тесты PetStore API с Allure отчетами и шагами
"""
import pytest
import allure
import random
from unittest.mock import Mock
from src.utils.allure_steps import PetStoreSteps, ValidationSteps


class MockPetStoreAPI:
    """Мок-класс для имитации PetStore API"""
    
    def __init__(self):
        self.pets = {}
        self.users = {}
        self.orders = {}
        self.inventory = {"available": 10, "pending": 5, "sold": 3}
        self.next_id = 1
    
    def add_pet(self, pet_data):
        pet_id = pet_data.get("id", self.next_id)
        self.next_id += 1
        self.pets[pet_id] = pet_data
        return self._create_response(200, pet_data)
    
    def get_pet(self, pet_id):
        if pet_id in self.pets:
            return self._create_response(200, self.pets[pet_id])
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def update_pet(self, pet_data):
        pet_id = pet_data["id"]
        if pet_id in self.pets:
            self.pets[pet_id] = pet_data
            return self._create_response(200, pet_data)
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def delete_pet(self, pet_id):
        if pet_id in self.pets:
            del self.pets[pet_id]
            return self._create_response(200, {"code": 200, "type": "unknown", "message": str(pet_id)})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def find_pets_by_status(self, status):
        pets_with_status = [pet for pet in self.pets.values() if pet.get("status") == status]
        return self._create_response(200, pets_with_status)
    
    def update_pet_with_form(self, pet_id, name=None, status=None):
        if pet_id in self.pets:
            if name:
                self.pets[pet_id]["name"] = name
            if status:
                self.pets[pet_id]["status"] = status
            return self._create_response(200, {"code": 200, "message": "success"})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def get_inventory(self):
        return self._create_response(200, self.inventory)
    
    def place_order(self, order_data):
        order_id = order_data.get("id", self.next_id)
        self.next_id += 1
        self.orders[order_id] = order_data
        return self._create_response(200, order_data)
    
    def get_order(self, order_id):
        if order_id in self.orders:
            return self._create_response(200, self.orders[order_id])
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Order not found"})
    
    def delete_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            return self._create_response(200, {"code": 200, "type": "unknown", "message": str(order_id)})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Order not found"})
    
    def create_user(self, user_data):
        username = user_data.get("username", f"user{self.next_id}")
        self.next_id += 1
        self.users[username] = user_data
        return self._create_response(200, {"code": 200, "type": "unknown", "message": str(user_data.get("id", ""))})
    
    def get_user(self, username):
        if username in self.users:
            return self._create_response(200, self.users[username])
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "User not found"})
    
    def update_user(self, username, user_data):
        if username in self.users:
            self.users[username] = user_data
            return self._create_response(200, {"code": 200, "type": "unknown", "message": str(user_data.get("id", ""))})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "User not found"})
    
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            return self._create_response(200, {"code": 200, "type": "unknown", "message": username})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "User not found"})
    
    def create_users_with_list(self, users_data):
        for user in users_data:
            username = user.get("username")
            if username:
                self.users[username] = user
        return self._create_response(200, {"code": 200, "type": "unknown", "message": "ok"})
    
    def create_users_with_array(self, users_data):
        for user in users_data:
            username = user.get("username")
            if username:
                self.users[username] = user
        return self._create_response(200, {"code": 200, "type": "unknown", "message": "ok"})
    
    def user_login(self, username, password):
        return self._create_response(200, {
            "code": 200, 
            "type": "unknown", 
            "message": f"logged in session: {random.randint(1000000, 9999999)}"
        })
    
    def user_logout(self):
        return self._create_response(200, {"code": 200, "type": "unknown", "message": "ok"})
    
    def _create_response(self, status_code, json_data):
        response = Mock()
        response.status_code = status_code
        response.json = Mock(return_value=json_data)
        return response


@allure.epic("PetStore API")
@allure.feature("Pet Management")
class TestPetEndpoints:
    """Тесты для эндпоинтов питомцев"""
    
    @pytest.fixture
    def api(self):
        return MockPetStoreAPI()
    
    @allure.story("Добавление питомцев")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_pet(self, api):
        with allure.step("Подготовка тестовых данных"):
            pet_data = {
                "id": 1,
                "name": "TestDog",
                "photoUrls": ["https://example.com/photo.jpg"],
                "tags": [{"id": 1, "name": "friendly"}],
                "status": "available"
            }
        
        with allure.step("Выполнить добавление питомца"):
            response = PetStoreSteps.add_pet(api, pet_data)
        
        with allure.step("Проверить успешный ответ"):
            ValidationSteps.validate_status_code(response, 200)
            data = response.json()
            ValidationSteps.validate_field_value(data, "name", "TestDog")
            ValidationSteps.validate_field_value(data, "status", "available")
    
    @allure.story("Получение информации о питомце")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_pet(self, api):
        with allure.step("Подготовка: добавить тестового питомца"):
            pet_data = {"id": 1, "name": "TestDog", "photoUrls": []}
            PetStoreSteps.add_pet(api, pet_data)
        
        with allure.step("Выполнить получение питомца"):
            response = PetStoreSteps.get_pet(api, 1)
        
        with allure.step("Проверить данные питомца"):
            ValidationSteps.validate_status_code(response, 200)
            data = response.json()
            ValidationSteps.validate_field_value(data, "id", 1)
            ValidationSteps.validate_field_value(data, "name", "TestDog")
    
    @allure.story("Обновление информации о питомце")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_pet(self, api):
        with allure.step("Подготовка: добавить питомца"):
            pet_data = {"id": 1, "name": "OldName", "photoUrls": []}
            PetStoreSteps.add_pet(api, pet_data)
        
        with allure.step("Выполнить обновление питомца"):
            updated_data = {"id": 1, "name": "NewName", "photoUrls": [], "status": "sold"}
            response = PetStoreSteps.update_pet(api, updated_data)
        
        with allure.step("Проверить обновленные данные"):
            ValidationSteps.validate_status_code(response, 200)
            data = response.json()
            ValidationSteps.validate_field_value(data, "name", "NewName")
            ValidationSteps.validate_field_value(data, "status", "sold")
    
    @allure.story("Удаление питомца")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_pet(self, api):
        with allure.step("Подготовка: добавить питомца"):
            pet_data = {"id": 1, "name": "TestDog", "photoUrls": []}
            PetStoreSteps.add_pet(api, pet_data)
        
        with allure.step("Проверить что питомец существует"):
            response = PetStoreSteps.get_pet(api, 1)
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Выполнить удаление питомца"):
            response = PetStoreSteps.delete_pet(api, 1)
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Проверить что питомец удален"):
            response = PetStoreSteps.get_pet(api, 1)
            ValidationSteps.validate_status_code(response, 404)
    
    @allure.story("Поиск питомцев по статусу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_find_pets_by_status(self, api):
        with allure.step("Подготовка: добавить питомцев с разными статусами"):
            PetStoreSteps.add_pet(api, {"id": 1, "name": "Dog1", "status": "available", "photoUrls": []})
            PetStoreSteps.add_pet(api, {"id": 2, "name": "Dog2", "status": "sold", "photoUrls": []})
            PetStoreSteps.add_pet(api, {"id": 3, "name": "Dog3", "status": "available", "photoUrls": []})
        
        with allure.step("Поиск питомцев со статусом available"):
            response = PetStoreSteps.find_pets_by_status(api, "available")
            ValidationSteps.validate_status_code(response, 200)
            pets = response.json()
            ValidationSteps.validate_response_is_list(pets)
            assert len(pets) == 2
            assert all(pet["status"] == "available" for pet in pets)


@allure.epic("PetStore API")
@allure.feature("Store Management")
class TestStoreEndpoints:
    """Тесты для эндпоинтов магазина"""
    
    @pytest.fixture
    def api(self):
        return MockPetStoreAPI()
    
    @allure.story("Получение инвентаря")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_inventory(self, api):
        with allure.step("Выполнить получение инвентаря"):
            response = PetStoreSteps.get_inventory(api)
        
        with allure.step("Проверить структуру инвентаря"):
            ValidationSteps.validate_status_code(response, 200)
            inventory = response.json()
            ValidationSteps.validate_response_is_dict(inventory)
            ValidationSteps.validate_response_contains_field(inventory, "available")
            ValidationSteps.validate_response_contains_field(inventory, "pending")
            ValidationSteps.validate_response_contains_field(inventory, "sold")
    
    @allure.story("Управление заказами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_workflow(self, api):
        with allure.step("Создать тестовые данные заказа"):
            order_data = {
                "id": 1,
                "petId": 123,
                "quantity": 1,
                "shipDate": "2023-12-07T10:00:00.000Z",
                "status": "placed",
                "complete": True
            }
        
        with allure.step("Разместить заказ"):
            response = PetStoreSteps.place_order(api, order_data)
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Получить заказ по ID"):
            response = PetStoreSteps.get_order(api, 1)
            ValidationSteps.validate_status_code(response, 200)
            data = response.json()
            ValidationSteps.validate_field_value(data, "id", 1)
            ValidationSteps.validate_field_value(data, "status", "placed")
        
        with allure.step("Удалить заказ"):
            response = PetStoreSteps.delete_order(api, 1)
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Проверить что заказ удален"):
            response = PetStoreSteps.get_order(api, 1)
            ValidationSteps.validate_status_code(response, 404)


@allure.epic("PetStore API")
@allure.feature("User Management")
class TestUserEndpoints:
    """Тесты для эндпоинтов пользователей"""
    
    @pytest.fixture
    def api(self):
        return MockPetStoreAPI()
    
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_workflow(self, api):
        with allure.step("Создать тестового пользователя"):
            user_data = {
                "id": 1,
                "username": "testuser",
                "firstName": "Test",
                "lastName": "User",
                "email": "test@example.com"
            }
            response = PetStoreSteps.create_user(api, user_data)
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Получить пользователя по имени"):
            response = PetStoreSteps.get_user(api, "testuser")
            ValidationSteps.validate_status_code(response, 200)
            data = response.json()
            ValidationSteps.validate_field_value(data, "username", "testuser")
            ValidationSteps.validate_field_value(data, "email", "test@example.com")
        
        with allure.step("Обновить пользователя"):
            updated_data = {"username": "testuser", "firstName": "Updated", "email": "updated@example.com"}
            response = PetStoreSteps.update_user(api, "testuser", updated_data)
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Проверить обновленные данные"):
            response = PetStoreSteps.get_user(api, "testuser")
            data = response.json()
            ValidationSteps.validate_field_value(data, "firstName", "Updated")
            ValidationSteps.validate_field_value(data, "email", "updated@example.com")
        
        with allure.step("Удалить пользователя"):
            response = PetStoreSteps.delete_user(api, "testuser")
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Проверить что пользователь удален"):
            response = PetStoreSteps.get_user(api, "testuser")
            ValidationSteps.validate_status_code(response, 404)
    
    @allure.story("Создание нескольких пользователей")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_multiple_users(self, api):
        with allure.step("Создать список пользователей"):
            users_data = [
                {"id": 1, "username": "user1", "firstName": "User1"},
                {"id": 2, "username": "user2", "firstName": "User2"}
            ]
            response = PetStoreSteps.create_users_with_list(api, users_data)
            ValidationSteps.validate_status_code(response, 200)
        
        with allure.step("Проверить созданных пользователей"):
            response1 = PetStoreSteps.get_user(api, "user1")
            response2 = PetStoreSteps.get_user(api, "user2")
            ValidationSteps.validate_status_code(response1, 200)
            ValidationSteps.validate_status_code(response2, 200)
    
    @allure.story("Аутентификация пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_login_logout(self, api):
        with allure.step("Выполнить логин пользователя"):
            response = PetStoreSteps.user_login(api, "test", "password")
            ValidationSteps.validate_status_code(response, 200)
            data = response.json()
            ValidationSteps.validate_response_contains_field(data, "message")
        
        with allure.step("Выполнить логаут пользователя"):
            response = PetStoreSteps.user_logout(api)
            ValidationSteps.validate_status_code(response, 200)
            data = response.json()
            ValidationSteps.validate_field_value(data, "message", "ok")


@allure.epic("PetStore API")
@allure.feature("Error Handling")
class TestErrorScenarios:
    """Тесты для обработки ошибок"""
    
    @pytest.fixture
    def api(self):
        return MockPetStoreAPI()
    
    @allure.story("Обработка несуществующих ресурсов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_nonexistent_resources(self, api):
        with allure.step("Проверить несуществующего питомца"):
            response = PetStoreSteps.get_pet(api, 999)
            ValidationSteps.validate_status_code(response, 404)
        
        with allure.step("Проверить несуществующий заказ"):
            response = PetStoreSteps.get_order(api, 999)
            ValidationSteps.validate_status_code(response, 404)
        
        with allure.step("Проверить несуществующего пользователя"):
            response = PetStoreSteps.get_user(api, "nonexistent")
            ValidationSteps.validate_status_code(response, 404)