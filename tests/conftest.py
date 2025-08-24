import pytest
from config import Config
from tests.pages.reqres_api import ReqresAPI
from tests.pages.dummy_api import DummyAPI


@pytest.fixture(scope="module")
def reqres_api():
    auth_headers = {
        "x-api-key": Config.X_API_KEY,
    }
    api = ReqresAPI(headers=auth_headers)
    return api


@pytest.fixture(scope="module")
def dummy_api():
    api = DummyAPI()
    return api
