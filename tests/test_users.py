from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE_URL = "/api/v1/users"
HEADERS = {"token": "fake-super-secret-token"}

def test_create_user_with_auth():
    """Creating a user with valid token should succeed."""
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

def test_create_user_missing_email_should_fail():
    """Creating a user without email should fail with 422 (validation error)."""
    response = client.post(
        BASE_URL,
        json={"username": "missing_email"},
        headers=HEADERS
    )
    assert response.status_code == 422

def test_create_user_without_auth():
    """Creating a user without token should still succeed (public route)."""
    response = client.post(
        BASE_URL,
        json={"username": "unauth", "email": "unauth@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "unauth"
    assert data["email"] == "unauth@example.com"

def test_list_users_with_auth():
    """Listing users with valid token should return a list."""
    response = client.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_users_without_auth_should_fail():
    """Listing users without token should return 401 Unauthorized."""
    response = client.get(BASE_URL)
    assert response.status_code == 401