import requests
from jsonschema import validate


def test_auth_token(base_url_fixture, token_schema_fixture):
    payload = {'username': 'admin', 'password': 'password123'}
    resp = requests.post(f'{base_url_fixture}/auth', json=payload, timeout=5)
    assert resp.status_code == 200
    validate(resp.json(), token_schema_fixture)
