"""Automated tests for the Flask API endpoints."""
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_hello_default(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, World!'}


def test_hello_with_name(client):
    response = client.get('/hello?name=Vivianna')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, Vivianna!'}


def test_sum_valid(client):
    response = client.post('/sum', json={'numbers': [1, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {'numbers': [1, 2, 3], 'sum': 6}


def test_sum_missing_field(client):
    response = client.post('/sum', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()


def test_sum_invalid_values(client):
    response = client.post('/sum', json={'numbers': [1, 'two', 3]})
    assert response.status_code == 400
    assert 'error' in response.get_json()


def test_sum_empty_list(client):
    response = client.post('/sum', json={'numbers': []})
    assert response.status_code == 400
    assert 'error' in response.get_json()


def test_sum_malformed_json(client):
    response = client.post('/sum', data='{"numbers": [1, 2,}', content_type='application/json')
    assert response.status_code == 400
    assert 'error' in response.get_json()


def test_sum_non_json(client):
    response = client.post('/sum', data='numbers=1,2,3')
    assert response.status_code == 400
    assert 'error' in response.get_json()
