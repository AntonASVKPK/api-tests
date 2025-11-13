import requests
import logging
from typing import Optional, Dict, Any, List

logger = logging.getLogger(__name__)


class PetStoreClient:
    def __init__(self, base_url: str = "https://petstore.swagger.io/v2"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Making {method} request to {url}")
        
        response = self.session.request(method, url, **kwargs)
        logger.info(f"Response status: {response.status_code}")
        
        return response

    def get_pet_by_id(self, pet_id: int) -> requests.Response:
        return self._request("GET", f"/pet/{pet_id}")

    def add_pet(self, pet_data: Dict[str, Any]) -> requests.Response:
        return self._request("POST", "/pet", json=pet_data)

    def update_pet(self, pet_data: Dict[str, Any]) -> requests.Response:
        return self._request("PUT", "/pet", json=pet_data)

    def delete_pet(self, pet_id: int) -> requests.Response:
        return self._request("DELETE", f"/pet/{pet_id}")

    def find_pets_by_status(self, status: str) -> requests.Response:
        return self._request("GET", f"/pet/findByStatus?status={status}")

    def update_pet_with_form(self, pet_id: int, name: str = None, status: str = None) -> requests.Response:
        data = {}
        if name:
            data["name"] = name
        if status:
            data["status"] = status
        
        return self._request("POST", f"/pet/{pet_id}", data=data)

    def get_inventory(self) -> requests.Response:
        return self._request("GET", "/store/inventory")

    def place_order(self, order_data: Dict[str, Any]) -> requests.Response:
        return self._request("POST", "/store/order", json=order_data)

    def get_order_by_id(self, order_id: int) -> requests.Response:
        return self._request("GET", f"/store/order/{order_id}")

    def delete_order(self, order_id: int) -> requests.Response:
        return self._request("DELETE", f"/store/order/{order_id}")

    def create_user(self, user_data: Dict[str, Any]) -> requests.Response:
        return self._request("POST", "/user", json=user_data)

    def create_users_with_list(self, users_data: List[Dict[str, Any]]) -> requests.Response:
        return self._request("POST", "/user/createWithList", json=users_data)

    def create_users_with_array(self, users_data: List[Dict[str, Any]]) -> requests.Response:
        return self._request("POST", "/user/createWithArray", json=users_data)

    def get_user_by_username(self, username: str) -> requests.Response:
        return self._request("GET", f"/user/{username}")

    def update_user(self, username: str, user_data: Dict[str, Any]) -> requests.Response:
        return self._request("PUT", f"/user/{username}", json=user_data)

    def delete_user(self, username: str) -> requests.Response:
        return self._request("DELETE", f"/user/{username}")

    def user_login(self, username: str, password: str) -> requests.Response:
        return self._request("GET", f"/user/login?username={username}&password={password}")

    def user_logout(self) -> requests.Response:
        return self._request("GET", "/user/logout")