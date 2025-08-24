import requests
from requests import Response
from config import Config


class DummyAPI:
    def __init__(self):
        self.base_url = Config.DUMMY_BASE_URL

    def products_search(self, product_type: str) -> Response:
        response = requests.get(f"{self.base_url}/products/search", params={"q": product_type})
        return response

    def authenticate(self, user_creds: dict) -> Response:
        response = requests.post(f"{self.base_url}/auth/login", json=user_creds)
        return response

    def get_user_data(self, user_creds: dict, headers: dict | None) -> Response:
        response = requests.get(f"{self.base_url}/auth/me", json=user_creds, headers=headers)
        return response
