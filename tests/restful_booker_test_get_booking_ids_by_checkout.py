import requests

base_url = "https://restful-booker.herokuapp.com"

def test_get_booking_ids_by_checkout():
    response = requests.get(f"{base_url}/booking?checkin=<2026-08-01")
    assert response.status_code == 200
    body = response.json()
    assert len(body) > 0
    print(body)