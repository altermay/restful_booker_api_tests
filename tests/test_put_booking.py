import requests

base_url = "https://restful-booker.herokuapp.com"

def test_put_booking():

    create_payload = {
        "firstname": "Hanako",
        "lastname": "Suzuki",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-09-01",
            "checkout": "2026-09-02"
        },
        "additionalneeds": "Launch"
    }

    create_response = requests.post(f"{base_url}/booking", json=create_payload)
    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    auth_response = requests.post(f"{base_url}/auth",json={"username":"admin","password":"password123"})
    assert auth_response.status_code == 200
    token = auth_response.json()["token"]

    headers = {"Cookie": f"token={token}"}

    payload = {
        "firstname": "Hanako_updated",
        "lastname": "Suzuki_updated",
        "totalprice": 2000,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-09-03",
            "checkout": "2026-09-04"
        },
        "additionalneeds": "Dinner"
    }

    response = requests.put(f"{base_url}/booking/{booking_id}", headers=headers, json=payload)
    assert response.status_code == 200
    body = response.json()

    assert body["firstname"] == payload["firstname"]
    assert body["lastname"] == payload["lastname"]
    assert body["totalprice"] == payload["totalprice"]
    assert body["depositpaid"] == payload["depositpaid"]
    assert body["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert body["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]
    assert body["additionalneeds"] == payload["additionalneeds"]
