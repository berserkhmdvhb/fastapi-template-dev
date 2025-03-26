from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE_URL = "/api/v1/users"
HEADERS = {"token": "fake-super-secret-token"}

def test_create_user_success():
    response = client.post(
        BASE_URL,
        json={"username": "john", "email": "john@example.com"},
        headers=HEADERS
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "john"
    assert data["email"] == "john@example.com"
    assert "id" in data

def test_create_user_missing_email():
    response = client.post(
        BASE_URL,
        json={"username": "missing_email"},
        headers=HEADERS
    )
    assert response.status_code == 422

def test_create_user_unauthorized():
    response = client.post(
        BASE_URL,
        json={"username": "unauth", "email": "unauth@example.com"}
    )
    assert response.status_code == 401

def test_list_users_authenticated():
    response = client.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_users_unauthenticated():
    response = client.get(BASE_URL)
    assert response.status_code == 401
