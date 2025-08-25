import requests
from requests import Response
from config import Config


class BookerAPI:
    def __init__(self):
        self.base_url = Config.BOOKER_BASE_URL

    def create_booking(self, data: str, headers: None | dict = None) -> Response:
        response = requests.post(f"{self.base_url}/booking", data=data, headers=headers)
        return response

    def check_booking(self, booking_id: str) -> Response:
        response = requests.get(f"{self.base_url}/booking/{booking_id}")
        return response

    def get_token(self) -> Response:
        response = requests.post(
            f"{self.base_url}/auth",
            json={
                "username": "admin",
                "password": "password123"
            }
        )
        return response

    def update_booking(self, id: int, data: str, cookies: dict = None, headers: None | dict = None) -> Response:
        if headers is None:
            headers = {}
        headers["Content-Type"] = "application/json"

        response = requests.put(
            f"{self.base_url}/booking/{id}",
            data=data,
            headers=headers,
            cookies=cookies
        )
        return response

    def partly_update_booking(self, id: int, data: dict, cookies: dict = None) -> Response:

        response = requests.patch(
            f"{self.base_url}/booking/{id}",
            data=data,
            cookies=cookies
        )
        return response

    def delete_booking(self, id: int, cookies: dict = None) -> Response:
        response = requests.delete(
            f"{self.base_url}/booking/{id}",
            cookies=cookies
        )
        return response