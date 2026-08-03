import requests

base_url = "https://restful-booker.herokuapp.com"

def test_create_booking():
    payload = {
        "firstname": "Taro",
        "lastname": "Yamada",
        "totalprice": 1050,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-09-01",
            "checkout": "2026-09-02"
        },
        "additionalneeds": "Launch"
    }

    response = requests.post(f"{base_url}/booking", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    print("Booking ID:", body["bookingid"])