import requests

base_url = "https://restful-booker.herokuapp.com"

def test_get_booking():
    response = requests.get(f"{base_url}/booking/2216")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    body = response.json()
    assert "firstname" in body
    assert "lastname" in body
    assert "totalprice" in body
    assert "depositpaid" in body
    assert "bookingdates" in body
    assert "checkin" in body["bookingdates"]
    assert "checkout" in body["bookingdates"]