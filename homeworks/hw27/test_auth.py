# pylint: disable=R0801
import pathlib
import json
import requests
from jsonschema import validate


def test_auth_token(base_url_fixture, token_schema_fixture):
    payload_path = pathlib.Path(__file__).parent / 'data' / 'login_data.json'
    with payload_path.open() as f:
        payload = json.load(f)
    resp = requests.post(f'{base_url_fixture}/auth', json=payload, timeout=5)
    assert resp.status_code == 200
    validate(resp.json(), token_schema_fixture)
