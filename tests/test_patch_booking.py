import requests

base_url = "https://restful-booker.herokuapp.com"

def test_patch_booking():

    create_payload = {
        "firstname": "Taro",
        "lastname": "Yamada",
        "totalprice": 1050,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-02"
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
        "bookingdates": {
            "checkin": "2026-11-01",
            "checkout": "2026-11-02"
        }
    }

    response = requests.patch(f"{base_url}/booking/{booking_id}", headers=headers, json=payload)
    assert response.status_code == 200
    body = response.json()

    assert body["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert body["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]