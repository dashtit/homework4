import requests
from jsonschema import validate


def test_get_all_bookings(base_url_fixture):
    resp = requests.get(f'{base_url_fixture}/booking', timeout=5)
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_create_booking(base_url_fixture, booking_data_fixture, booking_schema_fixture):
    resp = requests.post(f'{base_url_fixture}/booking', json=booking_data_fixture, timeout=5)
    assert resp.status_code == 200
    validate(resp.json(), booking_schema_fixture)


def test_get_booking_by_id(base_url_fixture, created_booking_fixture, booking_data_fixture):
    resp = requests.get(f'{base_url_fixture}/booking/{created_booking_fixture}', timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert data['firstname'] == booking_data_fixture['firstname']
    assert data['lastname'] == booking_data_fixture['lastname']


def test_update_booking(base_url_fixture, created_booking_fixture, auth_token_fixture):
    payload = {
        'firstname': 'Alice',
        'lastname': 'Smith',
        'totalprice': 200,
        'depositpaid': False,
        'bookingdates': {'checkin': '2024-02-01', 'checkout': '2024-02-05'}
    }
    cookies = {'token': auth_token_fixture}
    resp = requests.put(f'{base_url_fixture}/booking/{created_booking_fixture}',
                        json=payload, cookies=cookies, timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert data['firstname'] == 'Alice'
    assert data['lastname'] == 'Smith'


def test_partial_update_booking(base_url_fixture, created_booking_fixture, auth_token_fixture):
    payload = {'firstname': 'Bob'}
    cookies = {'token': auth_token_fixture}
    resp = requests.patch(f'{base_url_fixture}/booking/{created_booking_fixture}',
                          json=payload, cookies=cookies, timeout=5)
    assert resp.status_code == 200
    assert resp.json()['firstname'] == 'Bob'


def test_delete_booking(base_url_fixture, booking_data_fixture, auth_token_fixture):
    resp_create = requests.post(f'{base_url_fixture}/booking',
                                json=booking_data_fixture, timeout=5)
    booking_id = resp_create.json()['bookingid']
    cookies = {'token': auth_token_fixture}
    resp_delete = requests.delete(f'{base_url_fixture}/booking/{booking_id}',
                                  cookies=cookies, timeout=5)
    assert resp_delete.status_code == 201


def test_filter_booking_by_firstname(base_url_fixture):
    resp = requests.get(f'{base_url_fixture}/booking?firstname=John', timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
