import requests

base_url = "https://restful-booker.herokuapp.com"

def test_create_booking():
    payload = {
        "firstname": "Mariko",
        "lastname": "Tanaka",
        "totalprice": 3000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2027-01-01",
            "checkout": "2027-01-02"
        },
        "additionalneeds": "Launch"
    }

    response = requests.post(f"{base_url}/booking", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body