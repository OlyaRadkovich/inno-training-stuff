import pytest
from config import Config
from tests.pages.reqres_api import ReqresApi


@pytest.fixture(scope="module")
def reqres_api():
    auth_headers = {
        "x-api-key": Config.X_API_KEY,
    }
    api = ReqresApi(headers=auth_headers)
    return api
