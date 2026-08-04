import requests

base_url = "https://restful-booker.herokuapp.com"

def test_put_booking():

    auth_response = requests.post(f"{base_url}/auth",json={"username":"admin","password":"password123"})
    assert auth_response.status_code == 200
    token = auth_response.json()["token"]

    headers = {"Cookie": f"token={token}"}

    payload = {
        "firstname": "Taro",
        "lastname": "Doe",
        "totalprice": 1050,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-02"
        },
        "additionalneeds": "Launch"
    }

    response = requests.put(f"{base_url}/booking/1698", headers=headers, json=payload)
    assert response.status_code == 200
    body = response.json()

    assert body["firstname"] == payload["firstname"]
    assert body["lastname"] == payload["lastname"]
    assert body["totalprice"] == payload["totalprice"]
    assert body["depositpaid"] == payload["depositpaid"]
    assert body["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]
    assert body["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"]
    assert body["additionalneeds"] == payload["additionalneeds"]
