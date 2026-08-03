import requests

base_url = "https://restful-booker.herokuapp.com"

def test_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(f"{base_url}/auth", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "token" in body




