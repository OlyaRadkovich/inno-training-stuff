import pytest
from config import Config
from datetime import datetime
from tests.pages.reqres_api import ReqresAPI


@pytest.mark.reqres
@pytest.mark.id("TC-API-01")
def test_get_users_list(reqres_api: ReqresAPI):
    """
    TC-API-01: Verify that GET /users?page=2 returns 200 and data contains 6 users
    """
    req = reqres_api.get_users_list(2)
    response = req.json()
    assert req.status_code == 200, f"Expected status code 200 but got {req.status_code}"
    assert response["page"] == 2, f"Expected page=2 but got {response['page']}"
    assert isinstance(response["data"], list), f"Expected 'data' to be a list but got {type(response['data'])}"
    assert len(response["data"]) == 6, f"Expected 6 objects in 'data' but got {len(response['data'])}"


@pytest.mark.reqres
@pytest.mark.id("TC-API-02")
def test_get_user(reqres_api: ReqresAPI):
    """
    TC-API-02: Verify that GET /users/2 returns 200, data contains id = 2 and email = 'janet.weaver@reqres.in.'
    """
    req = reqres_api.get_user(2)
    response = req.json()
    assert req.status_code == 200, f"Expected status code 200 but got {req.status_code}"
    assert response["data"]["id"] == 2, f"Expected id=2 but got {response['page']}"
    assert response["data"][
               "email"] == "janet.weaver@reqres.in", (f"Expected email to be 'janet.weaver@reqres.in' "
                                                      f"but got {response["data"]["email"]}")


@pytest.mark.reqres
@pytest.mark.id("TC-API-03")
def test_get_non_existent_user(reqres_api: ReqresAPI):
    """
    TC-API-03: Verify that GET /users/23 returns 404
    """
    req = reqres_api.get_user(23)
    assert req.status_code == 404, f"Expected status code 404 but got {req.status_code}"


@pytest.mark.reqres
@pytest.mark.id("TC-API-04")
def test_create_user(reqres_api: ReqresAPI):
    """
    TC-API-04: Create a new user, verify his name, job, id, date of creation
    """
    req = reqres_api.create_user(Config.new_user)
    response = req.json()
    assert req.status_code == 201, f"Expected status code 201 but got {req.status_code}"
    assert response["name"] == Config.new_user[
        "name"], f"Expected name {Config.new_user["name"]}  but got {response["data"]["name"]}"
    assert response["job"] == Config.new_user[
        "job"], f"Expected job {Config.new_user["job"]}  but got {response["data"]["job"]}"
    assert isinstance(response["id"], str)
    created_at = response["createdAt"]
    assert isinstance(created_at, str)
    try:
        if created_at.endswith('Z'):
            created_at = created_at[:-1] + '+00:00'
        datetime.fromisoformat(created_at)
    except ValueError:
        pytest.fail(f"'{response['createdAt']}' is not in a valid ISO 8601 format.")


@pytest.mark.reqres
@pytest.mark.id("TC-API-05")
def test_delete_user(reqres_api: ReqresAPI):
    """
    TC-API-05: Delete a user, verify status code of deletion
    """
    req = reqres_api.delete_user(2)
    assert req.status_code == 204, f"Expected status code 204 but got {req.status_code}"
