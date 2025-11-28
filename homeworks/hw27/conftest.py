# pylint: disable=redefined-outer-name
from datetime import date, timedelta
import random
import pathlib
import json
from jsonschema import validate
from faker import Faker
import requests
import pytest


BASE_URL = 'https://restful-booker.herokuapp.com'


fake = Faker()


@pytest.fixture
def base_url_fixture():
    return BASE_URL


@pytest.fixture
def token_schema_fixture():
    schema_path = pathlib.Path(__file__).parent / 'schemas' / 'jsonschema_sample_auth.json'
    with schema_path.open() as f:
        return json.load(f)


@pytest.fixture
def booking_schema_fixture():
    schema_path = pathlib.Path(__file__).parent / 'schemas' / 'jsonschema_sample_booking.json'
    with schema_path.open() as f:
        return json.load(f)


@pytest.fixture
def booking_data_fixture():
    checkin = date(2025, 1, 1) + timedelta(days=random.randint(0, 365))
    checkout = checkin + timedelta(days=random.randint(1, 14))
    return {
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'totalprice': random.randint(50, 500),
        'depositpaid': random.choice([True, False]),
        'bookingdates': {
            'checkin': checkin.isoformat(),
            'checkout': checkout.isoformat()
        },
        'additionalneeds': random.choice(['Breakfast', 'Lunch', 'None'])
    }


@pytest.fixture
def auth_token_fixture(base_url_fixture):
    payload_path = pathlib.Path(__file__).parent / 'data' / 'login_data.json'
    with payload_path.open() as f:
        payload = json.load(f)
    resp = requests.post(f'{base_url_fixture}/auth', json=payload, timeout=5)
    assert resp.status_code == 200
    return resp.json().get('token')


@pytest.fixture
def created_booking_fixture(base_url_fixture, booking_data_fixture, booking_schema_fixture):
    resp = requests.post(f'{base_url_fixture}/booking', json=booking_data_fixture, timeout=5)
    assert resp.status_code == 200
    validate(resp.json(), booking_schema_fixture)
    return resp.json()['bookingid']
