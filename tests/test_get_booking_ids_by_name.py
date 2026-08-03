import requests

base_url = "https://restful-booker.herokuapp.com"

def test_get_booking_ids_by_name():
    response = requests.get(f"{base_url}/booking?firstname=Taro&lastname=Yamada")
    assert response.status_code == 200
    body = response.json()
    assert len(body) > 0
    print(body)