# test_bookings.py

import requests



BOOKINGS_URL = "https://restful-booker.herokuapp.com/booking"
SUCCESS_CODE = 200
BOOKING_DATA = {'firstname': 'Carlos', 'lastname': 'Frias', 'totalprice': 128, 'depositpaid': True, 'bookingdates': {'checkin': '2026-11-18', 'checkout': '2026-11-30'}}


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
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    server_response = requests.post(BOOKINGS_URL, json=BOOKING_DATA, headers=headers)

    status_code = server_response.status_code
    print(status_code)
    assert status_code == SUCCESS_CODE, f"Status code does not match, got: {status_code}, Expected: {SUCCESS_CODE}"

    post_info = server_response.json()
    print(post_info)
    assert "bookingid" in post_info, f"bookingid has not been created, got: {post_info}"
    assert BOOKING_DATA['lastname'] == post_info['booking']['lastname'], f"booked last name does not match, got: {post_info['booking']['lastname']}, Expected: {BOOKING_DATA['lastname']}"


def test_create_and_get_booking():
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    server_response = requests.post(BOOKINGS_URL, json=BOOKING_DATA, headers=headers)
    post_status_code = server_response.status_code
    assert post_status_code == SUCCESS_CODE, f"POST Status code does not match, got: {post_status_code}, Expected: {SUCCESS_CODE}"

    booking_info = server_response.json()
    assert "bookingid" in booking_info, f"bookingid has not been created, got: {booking_info}"
    booking_id = booking_info["bookingid"]

    url = f"{BOOKINGS_URL}/{booking_id}"

    response_after_booking = requests.get(url, headers=headers)
    get_status_code = response_after_booking.status_code
    assert get_status_code == SUCCESS_CODE, f"GET Status code does not match, got: {get_status_code}, Expected: {SUCCESS_CODE}"
    data_response = response_after_booking.json()
    print(data_response)
    assert data_response['firstname'] == BOOKING_DATA['firstname'], f"First name does not match, got: {data_response['firstname']}, Expected: {BOOKING_DATA['firstname']}"
    assert data_response['lastname'] == BOOKING_DATA['lastname'], f"Last name does not match, got: {data_response['lastname']}, Expected: {BOOKING_DATA['lastname']}"