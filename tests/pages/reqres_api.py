import requests
from requests import Response
from config import Config


class ReqresAPI:
    def __init__(self, headers: dict | None = None):
        self.base_url = Config.REQRES_BASE_URL
        self.headers = headers if headers else {}

    def get_users_list(self, page_number: int) -> Response:
        response = requests.get(self.base_url, params={'page': page_number}, headers=self.headers)
        return response

    def get_user(self, user_id: int)  -> Response:
        return requests.get(f"{self.base_url}/{user_id}", headers=self.headers)

    def create_user(self, user_data: dict)  -> Response:
        response = requests.post(self.base_url, json=user_data, headers=self.headers)
        return response

    def delete_user(self, user_id: int)  -> Response:
        return requests.delete(f"{self.base_url}/{user_id}", headers=self.headers)
