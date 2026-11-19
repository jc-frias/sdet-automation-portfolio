# test_bookings.py

import requests



BOOKINGS_URL = "https://restful-booker.herokuapp.com/booking"
SUCCESS_CODE = 200


def test_if_booking_exists():
    booking_id = 1

    url = f"{BOOKINGS_URL}/{booking_id}"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)
    status_code = response.status_code
    print(status_code)
    assert status_code == SUCCESS_CODE, f"Status code does not match, got: {status_code}, Expected: {SUCCESS_CODE}"

    data = response.json()
    print(data)


def test_create_booking():
    data = {'firstname': 'Carlos', 'lastname': 'Frias', 'totalprice': 128, 'depositpaid': True, 'bookingdates': {'checkin': '2026-11-18', 'checkout': '2026-11-30'}}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    server_response = requests.post(BOOKINGS_URL, json=data, headers=headers)

    status_code = server_response.status_code
    print(status_code)
    assert status_code == SUCCESS_CODE, f"Status code does not match, got: {status_code}, Expected: {SUCCESS_CODE}"

    post_info = server_response.json()
    print(post_info)
    assert "bookingid" in post_info, f"bookingid has not been created, got: {post_info}"
    assert data['lastname'] == post_info['booking']['lastname'], f"booked last name does not match, got: {post_info['booking']['lastname']}, Expected: {data['lastname']}"

