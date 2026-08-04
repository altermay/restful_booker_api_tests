import requests

base_url = "https://restful-booker.herokuapp.com"

def test_delete_booking():

    create_payload = {
        "firstname": "Ichiro",
        "lastname": "Suzuki",
        "totalprice": 9999,
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

    response = requests.delete(f"{base_url}/booking/{booking_id}", headers=headers)
    assert response.status_code == 201

