class Config:
    # --------------------------------------------------
    REQRES_BASE_URL = "https://reqres.in/api/users"

    X_API_KEY = "reqres-free-v1"

    new_user = {
        "name": "Morpheus",
        "job": "Leader"
    }

    # --------------------------------------------------
    DUMMY_BASE_URL = "https://dummyjson.com"

    user_creds = {
        "username": "michaelw",
        "password": "michaelwpass"
    }

    invalid_user_creds = {
        "username": "michaelw",
        "password": "0lelplR"
    }

    # --------------------------------------------------
    BOOKER_BASE_URL = "https://restful-booker.herokuapp.com"

    payload = '''
    {
        "firstname": "Jim",
        "lastname": "Brown", 
        "totalprice": 111,
        "depositpaid": true, 
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-15"},
        "additionalneeds": "Breakfast"
    }
    '''

    new_payload = '''
        {
            "firstname": "Mary", 
            "lastname": "Brown", 
            "totalprice": 120,
            "depositpaid": true, 
            "bookingdates": {"checkin": "2024-01-26", "checkout": "2024-02-01"},
            "additionalneeds": "Breakfast"
        }
    '''

    partly_payload = {
        "firstname": "Freddy",
        "lastname": "Kruger"
    }

    e2e_payload = '''
        {
            "firstname": "Valya",
            "lastname": "Tereshkova", 
            "totalprice": 500,
            "depositpaid": false, 
            "bookingdates": {"checkin": "2025-10-10", "checkout": "2025-10-29"},
            "additionalneeds": "Jakuzi"
        }
    '''
