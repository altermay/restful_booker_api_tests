import requests

base_url = "https://restful-booker.herokuapp.com"

def test_delete_booking():

    auth_response = requests.post(f"{base_url}/auth",json={"username":"admin","password":"password123"})
    assert auth_response.status_code == 200
    token = auth_response.json()["token"]

    headers = {"Cookie": f"token={token}"}

    response = requests.delete(f"{base_url}/booking/126370", headers=headers)
    assert response.status_code == 201

