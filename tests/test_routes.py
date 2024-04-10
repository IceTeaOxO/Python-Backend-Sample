import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'hello world!' in response.data

def test_api_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_api_create_user(client):
    new_user_data = {'username': 'john_doe', 'email': 'john_doe@example.com'}
    response = client.post('/api/user', json=new_user_data)
    assert response.status_code == 201
    assert response.content_type == 'application/json'
    data = json.loads(response.data)
    assert 'id' in data
    assert 'username' in data
    assert data['username'] == 'john_doe'
