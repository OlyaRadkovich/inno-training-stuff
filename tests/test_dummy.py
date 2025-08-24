import pytest
from tests.pages.dummy_api import DummyAPI
from config import Config
import pytest_check as check


@pytest.mark.dummy
@pytest.mark.id("TC-API-06")
def test_products_search(dummy_api: DummyAPI):
    """
    TC-API-06:  Verify that GET /products returns 200 and all products have brand='Apple'
    """
    req = dummy_api.products_search("iPhone")
    response = req.json()
    assert req.status_code == 200, f"Expected status code 200 but got {req.status_code}"
    assert "products" in response, "Response body does not contain 'products'"

    products = response["products"]

    for i, product in enumerate(products):
        check.equal(product["brand"], "Apple", f"Product #{i} (id={product['id']})")


@pytest.mark.dummy
@pytest.mark.id("TC-API-07")
def test_authenticate(dummy_api: DummyAPI):
    """
    TC-API-07:  Verify that response returns 200, token is a non-empty string, and username=Config.user_creds['username']
    """
    req = dummy_api.authenticate(Config.user_creds)
    response = req.json()
    assert req.status_code == 200, f"Expected status code 200 but got {req.status_code}"
    assert isinstance(response["accessToken"], str), "Response body does not contain 'token'"
    assert len(response["accessToken"]) > 0, "Access token is empty"
    assert response["username"] == Config.user_creds['username'], "Response body does not contain 'username'"


@pytest.mark.dummy
@pytest.mark.id("TC-API-08")
def test_authenticate_with_invalid_data(dummy_api: DummyAPI):
    """
    TC-API-08:  Verify that response returns 400, response contains message "Invalid credentials"
    """
    req = dummy_api.authenticate(Config.invalid_user_creds)
    response = req.json()
    assert req.status_code == 400, f"Expected status code 400 but got {req.status_code}"
    assert response['message'] == "Invalid credentials", f"Expected 'Invalid credentials' but got {response['message']}"


@pytest.mark.dummy
@pytest.mark.id("TC-API-09")
def test_get_user_profile_with_token(dummy_api: DummyAPI):
    """
    TC-API-09: Verify that GET /auth/me with valid token returns 200 and user data
    """
    auth_req = dummy_api.authenticate(Config.user_creds)
    response = auth_req.json()
    access_token = response["accessToken"]
    headers = {"Authorization": f"Bearer {access_token}"}
    req = dummy_api.get_user_data(Config.user_creds, headers=headers)
    response = req.json()
    assert req.status_code == 200, f"Expected status code 200 but got {req.status_code}"
    for field in ["id", "username", "email"]:
        assert field in response, f"Field '{field}' not found in response"
    assert len(response.keys()) > 3, "Response contains only minimal fields, expected more user data"


@pytest.mark.dummy
@pytest.mark.id("TC-API-10")
def test_get_user_profile_without_token(dummy_api: DummyAPI):
    """
    TC-API-10: Verify that GET /auth/me without Authorization header returns 401/403 with auth error message
    """
    req = dummy_api.get_user_data(Config.user_creds, headers=None)
    response = req.json()
    assert req.status_code == 401, f"Expected status code 401 but got {req.status_code}"
    assert response["message"] == "Access Token is required", f"Got message {response["message"]}"
