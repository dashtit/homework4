# pylint: disable=redefined-outer-name
import pytest
import requests
from jsonschema import validate


BASE_URL = 'https://restful-booker.herokuapp.com'


@pytest.fixture
def base_url_fixture():
    return BASE_URL


@pytest.fixture
def token_schema_fixture():
    return {
        'type': 'object',
        'properties': {
            'token': {'type': 'string'}
        },
        'required': ['token']
    }


@pytest.fixture
def booking_schema_fixture():
    return {
        'type': 'object',
        'properties': {
            'bookingid': {'type': 'integer'}
        },
        'required': ['bookingid']
    }


@pytest.fixture
def booking_data_fixture():
    return {
        'firstname': 'John',
        'lastname': 'Doe',
        'totalprice': 150,
        'depositpaid': True,
        'bookingdates': {'checkin': '2024-01-01', 'checkout': '2024-01-10'},
        'additionalneeds': 'Breakfast'
    }


@pytest.fixture
def auth_token_fixture(base_url_fixture):
    payload = {
        'username': 'admin',
        'password': 'password123'
    }
    resp = requests.post(f'{base_url_fixture}/auth', json=payload, timeout=5)
    assert resp.status_code == 200
    return resp.json().get('token')


@pytest.fixture
def created_booking_fixture(base_url_fixture, booking_data_fixture, booking_schema_fixture):
    resp = requests.post(f'{base_url_fixture}/booking', json=booking_data_fixture, timeout=5)
    assert resp.status_code == 200
    validate(resp.json(), booking_schema_fixture)
    return resp.json()['bookingid']
