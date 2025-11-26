import requests


def test_delete_nonexistent_booking(base_url_fixture, auth_token_fixture):
    cookies = {'token': auth_token_fixture}
    resp_all = requests.get(f'{base_url_fixture}/booking', timeout=5)
    existing_ids = {item["bookingid"] for item in resp_all.json()}
    nonexistent_id = max(existing_ids) + 1
    resp = requests.delete(f'{base_url_fixture}/booking/{nonexistent_id}',
                           cookies=cookies, timeout=5)
    assert resp.status_code in [404, 405]


def test_get_invalid_booking_id(base_url_fixture):
    resp = requests.get(f'{base_url_fixture}/booking/abc', timeout=5)
    assert resp.status_code == 404


def test_create_booking_invalid_payload(base_url_fixture):
    payload = {'firstname': 'User'}
    resp = requests.post(f'{base_url_fixture}/booking', json=payload, timeout=5)
    assert resp.status_code in [400, 500]


def test_update_booking_invalid_token(base_url_fixture, created_booking_fixture):
    payload = {
        'firstname': 'Umpa',
        'lastname': 'Lumpa',
        'totalprice': 200,
        'depositpaid': True,
        'bookingdates': {'checkin': '2024-02-01', 'checkout': '2024-02-05'}
    }
    resp = requests.put(f'{base_url_fixture}/booking/{created_booking_fixture}',
                        json=payload, cookies={'token': 'wrong'}, timeout=5)
    assert resp.status_code in [403, 401]


def test_update_booking_invalid_payload(base_url_fixture, auth_token_fixture,
                                        created_booking_fixture):
    payload = {'lastname': 'User'}
    cookies = {'token': auth_token_fixture}
    resp = requests.put(f'{base_url_fixture}/booking/{created_booking_fixture}',
                        json=payload, cookies=cookies, timeout=5)
    assert resp.status_code in [400, 500]


def test_part_update_booking_invalid_token(base_url_fixture, created_booking_fixture):
    payload = {'firstname': 'Hacker'}
    resp = requests.patch(f'{base_url_fixture}/booking/{created_booking_fixture}',
                          json=payload, cookies={'token': 'wrong'}, timeout=5)
    assert resp.status_code in [403, 401]


def test_delete_booking_invalid_token(base_url_fixture, created_booking_fixture):
    resp_delete = requests.delete(f'{base_url_fixture}/booking/{created_booking_fixture}',
                                  cookies={'token': 'wrong'}, timeout=5)
    assert resp_delete.status_code in [403, 401]
