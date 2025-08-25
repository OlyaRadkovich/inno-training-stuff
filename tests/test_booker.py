import json
import pytest
from tests.pages.booker_api import BookerAPI
from config import Config


@pytest.mark.booker
@pytest.mark.id("TC-API-11")
def test_create_booking(booker_api: BookerAPI):
    """
    TC-API-11: Verify that POST /booking creates booking with correct data
    """
    req = booker_api.create_booking(headers={"Content-Type": "application/json"}, data=Config.payload)
    response = req.json()
    assert req.status_code == 200, f"Expected status code 200 but got {req.status_code}"
    assert isinstance(response["bookingid"],
                      int), f"Expected 'bookingid' to be 'int', got {type(response['bookingid'])}"
    actual_booking = response["booking"]
    expected_booking = json.loads(Config.payload)

    for key in expected_booking:
        assert key in actual_booking, f"Key '{key}' not found in response"

    for key in expected_booking:
        assert actual_booking[key] == expected_booking[
            key], f"Expected {expected_booking[key]}, got {actual_booking[key]}"


@pytest.mark.booker
@pytest.mark.id("TC-API-12")
def test_get_token(booker_api: BookerAPI):
    """
    TC-API-12: Get a token for update/deletion
    """
    req = booker_api.get_token()
    response = req.json()
    assert req.status_code == 200, f"Expected status code 200 but got {req.status_code}"
    assert isinstance(response["token"], str), f"Expected 'token' to be 'str', got {type(response['token'])}"
    assert len(response["token"]) > 0, f"Expected 'token' to contain at least one character, got {response['token']}"


@pytest.mark.booker
@pytest.mark.id("TC-API-13")
def test_update_booking(booker_api: BookerAPI):
    """
    TC-API-13: Create a booking, get a token for update/deletion, and update the booking
    """
    req1 = booker_api.create_booking(headers={"Content-Type": "application/json"}, data=Config.payload)
    response = req1.json()
    booking_id = response["bookingid"]

    req2 = booker_api.get_token()
    response = req2.json()
    token = response["token"]

    req3 = booker_api.update_booking(
        booking_id,
        data=Config.new_payload,
        cookies={"token": token}
    )
    response = req3.json()
    expected_data = json.loads(Config.new_payload)

    assert req3.status_code == 200, f"Expected status code 200 but got {req3.status_code}"
    assert response["firstname"] == expected_data["firstname"]
    assert response["lastname"] == expected_data["lastname"]
    assert response["totalprice"] == expected_data["totalprice"]
    assert response["depositpaid"] == expected_data["depositpaid"]
    assert response["bookingdates"]["checkin"] == expected_data["bookingdates"]["checkin"]
    assert response["bookingdates"]["checkout"] == expected_data["bookingdates"]["checkout"]
    assert response["additionalneeds"] == expected_data["additionalneeds"]


@pytest.mark.booker
@pytest.mark.id("TC-API-14")
def test_partly_update_booking(booker_api: BookerAPI):
    """
    TC-API-14: Create a booking, get a token for update/deletion, and change firstname and lastname in the booking
    """
    req1 = booker_api.create_booking(headers={"Content-Type": "application/json"}, data=Config.payload)
    response = req1.json()
    booking_id = response["bookingid"]

    req2 = booker_api.get_token()
    response = req2.json()
    token = response["token"]

    req3 = booker_api.partly_update_booking(
        booking_id,
        Config.partly_payload,
        cookies={"token": token}
    )
    response = req3.json()
    expected_data = Config.partly_payload
    old_data = json.loads(Config.payload)

    assert req3.status_code == 200, f"Expected status code 200 but got {req3.status_code}"
    assert response["firstname"] == expected_data["firstname"]
    assert response["lastname"] == expected_data["lastname"]
    assert response["totalprice"] == old_data["totalprice"]
    assert response["depositpaid"] == old_data["depositpaid"]
    assert response["bookingdates"]["checkin"] == old_data["bookingdates"]["checkin"]
    assert response["bookingdates"]["checkout"] == old_data["bookingdates"]["checkout"]
    assert response["additionalneeds"] == old_data["additionalneeds"]


@pytest.mark.booker
@pytest.mark.id("TC-API-15")
def test_e2e_booking(booker_api: BookerAPI):
    """
    TC-API-15: Create a booking, check it, than delete and check deletion
    """
    get_token = booker_api.get_token()
    response = get_token.json()
    token = response["token"]

    creating_booking = booker_api.create_booking(headers={"Content-Type": "application/json"}, data=Config.e2e_payload)
    assert creating_booking.status_code == 200, f"Expected status code 200 but got {creating_booking.status_code}"

    response = creating_booking.json()
    booking_id = response["bookingid"]
    check_booking = booker_api.check_booking(booking_id)
    assert check_booking.status_code == 200, f"Expected status code 200 but got {check_booking.status_code}"

    delete_booking = booker_api.delete_booking(booking_id, cookies={"token": token})
    assert delete_booking.status_code == 201, f"Expected status code 201 but got {delete_booking.status_code}"

    check_deletion = booker_api.check_booking(booking_id)
    assert check_deletion.status_code == 404, f"Expected status code 201 but got {check_deletion.status_code}"
