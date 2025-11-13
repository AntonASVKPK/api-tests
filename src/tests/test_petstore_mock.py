"""
Мок-тесты для PetStore API
Работают без реального подключения к API
"""
import pytest
from unittest.mock import Mock, patch
import random


class MockPetStoreAPI:
    """Мок-класс для имитации PetStore API"""
    
    def __init__(self):
        self.pets = {}
        self.users = {}
        self.orders = {}
        self.inventory = {"available": 10, "pending": 5, "sold": 3}
        self.next_id = 1
    
    def add_pet(self, pet_data):
        """Добавление питомца"""
        pet_id = pet_data.get("id", self.next_id)
        self.next_id += 1
        self.pets[pet_id] = pet_data
        return self._create_response(200, pet_data)
    
    def get_pet(self, pet_id):
        """Получение питомца по ID"""
        if pet_id in self.pets:
            return self._create_response(200, self.pets[pet_id])
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def update_pet(self, pet_data):
        """Обновление питомца"""
        pet_id = pet_data["id"]
        if pet_id in self.pets:
            self.pets[pet_id] = pet_data
            return self._create_response(200, pet_data)
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def delete_pet(self, pet_id):
        """Удаление питомца"""
        if pet_id in self.pets:
            del self.pets[pet_id]
            return self._create_response(200, {"code": 200, "type": "unknown", "message": str(pet_id)})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def find_pets_by_status(self, status):
        """Поиск питомцев по статусу"""
        pets_with_status = [pet for pet in self.pets.values() if pet.get("status") == status]
        return self._create_response(200, pets_with_status)
    
    def update_pet_with_form(self, pet_id, name=None, status=None):
        """Обновление питомца через форму"""
        if pet_id in self.pets:
            if name:
                self.pets[pet_id]["name"] = name
            if status:
                self.pets[pet_id]["status"] = status
            return self._create_response(200, {"code": 200, "message": "success"})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Pet not found"})
    
    def get_inventory(self):
        """Получение инвентаря"""
        return self._create_response(200, self.inventory)
    
    def place_order(self, order_data):
        """Размещение заказа"""
        order_id = order_data.get("id", self.next_id)
        self.next_id += 1
        self.orders[order_id] = order_data
        return self._create_response(200, order_data)
    
    def get_order(self, order_id):
        """Получение заказа по ID"""
        if order_id in self.orders:
            return self._create_response(200, self.orders[order_id])
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Order not found"})
    
    def delete_order(self, order_id):
        """Удаление заказа"""
        if order_id in self.orders:
            del self.orders[order_id]
            return self._create_response(200, {"code": 200, "type": "unknown", "message": str(order_id)})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "Order not found"})
    
    def create_user(self, user_data):
        """Создание пользователя"""
        username = user_data.get("username", f"user{self.next_id}")
        self.next_id += 1
        self.users[username] = user_data
        return self._create_response(200, {"code": 200, "type": "unknown", "message": str(user_data.get("id", ""))})
    
    def get_user(self, username):
        """Получение пользователя"""
        if username in self.users:
            return self._create_response(200, self.users[username])
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "User not found"})
    
    def update_user(self, username, user_data):
        """Обновление пользователя"""
        if username in self.users:
            self.users[username] = user_data
            return self._create_response(200, {"code": 200, "type": "unknown", "message": str(user_data.get("id", ""))})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "User not found"})
    
    def delete_user(self, username):
        """Удаление пользователя"""
        if username in self.users:
            del self.users[username]
            return self._create_response(200, {"code": 200, "type": "unknown", "message": username})
        else:
            return self._create_response(404, {"code": 1, "type": "error", "message": "User not found"})
    
    def create_users_with_list(self, users_data):
        """Создание пользователей из списка"""
        for user in users_data:
            username = user.get("username")
            if username:
                self.users[username] = user
        return self._create_response(200, {"code": 200, "type": "unknown", "message": "ok"})
    
    def create_users_with_array(self, users_data):
        """Создание пользователей из массива"""
        for user in users_data:
            username = user.get("username")
            if username:
                self.users[username] = user
        return self._create_response(200, {"code": 200, "type": "unknown", "message": "ok"})
    
    def user_login(self, username, password):
        """Логин пользователя"""
        return self._create_response(200, {
            "code": 200, 
            "type": "unknown", 
            "message": f"logged in session: {random.randint(1000000, 9999999)}"
        })
    
    def user_logout(self):
        """Логаут пользователя"""
        return self._create_response(200, {"code": 200, "type": "unknown", "message": "ok"})
    
    def _create_response(self, status_code, json_data):
        """Создание мок-ответа"""
        response = Mock()
        response.status_code = status_code
        response.json = Mock(return_value=json_data)
        return response


class TestPetStoreMock:
    """Тестовый класс для мок-тестов PetStore API"""
    
    @pytest.fixture
    def api(self):
        return MockPetStoreAPI()
    
    # Pet Tests
    def test_add_pet(self, api):
        """Тест добавления питомца"""
        pet_data = {
            "id": 1,
            "name": "TestDog",
            "photoUrls": ["https://example.com/photo.jpg"],
            "tags": [{"id": 1, "name": "friendly"}],
            "status": "available"
        }
        
        response = api.add_pet(pet_data)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "TestDog"
        assert data["status"] == "available"
    
    def test_get_pet(self, api):
        """Тест получения питомца по ID"""
        pet_data = {"id": 1, "name": "TestDog", "photoUrls": []}
        api.add_pet(pet_data)
        
        response = api.get_pet(1)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "TestDog"
    
    def test_update_pet(self, api):
        """Тест обновления питомца"""
        pet_data = {"id": 1, "name": "OldName", "photoUrls": []}
        api.add_pet(pet_data)
        
        updated_data = {"id": 1, "name": "NewName", "photoUrls": [], "status": "sold"}
        response = api.update_pet(updated_data)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "NewName"
        assert data["status"] == "sold"
    
    def test_delete_pet(self, api):
        """Тест удаления питомца"""
        pet_data = {"id": 1, "name": "TestDog", "photoUrls": []}
        api.add_pet(pet_data)
        
        response = api.get_pet(1)
        assert response.status_code == 200
        
        response = api.delete_pet(1)
        assert response.status_code == 200
        
        response = api.get_pet(1)
        assert response.status_code == 404
    
    def test_find_pets_by_status(self, api):
        """Тест поиска питомцев по статусу"""
        api.add_pet({"id": 1, "name": "Dog1", "status": "available", "photoUrls": []})
        api.add_pet({"id": 2, "name": "Dog2", "status": "sold", "photoUrls": []})
        api.add_pet({"id": 3, "name": "Dog3", "status": "available", "photoUrls": []})
        
        response = api.find_pets_by_status("available")
        assert response.status_code == 200
        pets = response.json()
        assert len(pets) == 2
        assert all(pet["status"] == "available" for pet in pets)
    
    def test_update_pet_with_form(self, api):
        """Тест обновления питомца через форму"""
        pet_data = {"id": 1, "name": "Original", "status": "available", "photoUrls": []}
        api.add_pet(pet_data)
        
        response = api.update_pet_with_form(1, name="UpdatedName", status="pending")
        assert response.status_code == 200
        
        response = api.get_pet(1)
        data = response.json()
        assert data["name"] == "UpdatedName"
        assert data["status"] == "pending"
    
    def test_get_inventory(self, api):
        """Тест получения инвентаря"""
        response = api.get_inventory()
        assert response.status_code == 200
        inventory = response.json()
        assert "available" in inventory
        assert "pending" in inventory
        assert "sold" in inventory
    
    def test_place_and_get_order(self, api):
        """Тест размещения и получения заказа"""
        order_data = {
            "id": 1,
            "petId": 123,
            "quantity": 1,
            "shipDate": "2023-12-07T10:00:00.000Z",
            "status": "placed",
            "complete": True
        }
        
        response = api.place_order(order_data)
        assert response.status_code == 200
        
        response = api.get_order(1)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["status"] == "placed"
    
    def test_delete_order(self, api):
        """Тест удаления заказа"""
        order_data = {"id": 1, "petId": 123, "quantity": 1, "status": "placed"}
        api.place_order(order_data)
        
        response = api.delete_order(1)
        assert response.status_code == 200
        
        response = api.get_order(1)
        assert response.status_code == 404
    
    def test_create_and_get_user(self, api):
        """Тест создания и получения пользователя"""
        user_data = {
            "id": 1,
            "username": "testuser",
            "firstName": "Test",
            "lastName": "User",
            "email": "test@example.com"
        }
        
        response = api.create_user(user_data)
        assert response.status_code == 200
        
        response = api.get_user("testuser")
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"
    
    def test_update_user(self, api):
        """Тест обновления пользователя"""
        user_data = {"username": "testuser", "firstName": "OldName", "email": "old@example.com"}
        api.create_user(user_data)
        
        updated_data = {"username": "testuser", "firstName": "NewName", "email": "new@example.com"}
        response = api.update_user("testuser", updated_data)
        assert response.status_code == 200
        
        response = api.get_user("testuser")
        data = response.json()
        assert data["firstName"] == "NewName"
        assert data["email"] == "new@example.com"
    
    def test_delete_user(self, api):
        """Тест удаления пользователя"""
        user_data = {"username": "testuser", "firstName": "Test"}
        api.create_user(user_data)
        
        response = api.delete_user("testuser")
        assert response.status_code == 200
        
        response = api.get_user("testuser")
        assert response.status_code == 404
    
    def test_create_users_with_list(self, api):
        """Тест создания пользователей из списка"""
        users_data = [
            {"id": 1, "username": "user1", "firstName": "User1"},
            {"id": 2, "username": "user2", "firstName": "User2"}
        ]
        
        response = api.create_users_with_list(users_data)
        assert response.status_code == 200
        
        response1 = api.get_user("user1")
        response2 = api.get_user("user2")
        assert response1.status_code == 200
        assert response2.status_code == 200
    
    def test_create_users_with_array(self, api):
        """Тест создания пользователей из массива"""
        users_data = [
            {"id": 1, "username": "user3", "firstName": "User3"},
            {"id": 2, "username": "user4", "firstName": "User4"}
        ]
        
        response = api.create_users_with_array(users_data)
        assert response.status_code == 200
        
        response1 = api.get_user("user3")
        response2 = api.get_user("user4")
        assert response1.status_code == 200
        assert response2.status_code == 200
    
    def test_user_login_logout(self, api):
        """Тест входа и выхода пользователя"""
        response = api.user_login("test", "password")
        assert response.status_code == 200
        
        response = api.user_logout()
        assert response.status_code == 200
    
    def test_nonexistent_pet(self, api):
        """Тест получения несуществующего питомца"""
        response = api.get_pet(999)
        assert response.status_code == 404
    
    def test_nonexistent_order(self, api):
        """Тест получения несуществующего заказа"""
        response = api.get_order(999)
        assert response.status_code == 404
    
    def test_nonexistent_user(self, api):
        """Тест получения несуществующего пользователя"""
        response = api.get_user("nonexistent")
        assert response.status_code == 404


def test_with_patch():
    """Тест с использованием unittest.mock.patch"""
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"id": 1, "name": "TestDog"}
        
        import requests
        response = requests.post("https://petstore.swagger.io/v2/pet", json={"name": "TestDog"})
        
        assert response.status_code == 200
        assert response.json()["name"] == "TestDog"
        mock_post.assert_called_once()