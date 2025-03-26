from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
BASE_URL = "/api/v1/items"
HEADERS = {"token": "fake-super-secret-token"}

def test_create_item_success():
    response = client.post(
        BASE_URL,
        json={"name": "Notebook", "description": "A ruled notebook"},
        headers=HEADERS
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Notebook"

def test_create_item_missing_name():
    response = client.post(
        BASE_URL,
        json={"description": "Missing name field"},
        headers=HEADERS
    )
    assert response.status_code == 422  # Unprocessable Entity

def test_create_item_no_token():
    response = client.post(
        BASE_URL,
        json={"name": "Pen"}
    )
    assert response.status_code == 401

def test_list_items_authenticated():
    response = client.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_items_unauthenticated():
    response = client.get(BASE_URL)
    assert response.status_code == 401

def test_invalid_route():
    response = client.get("/api/v1/invalid")
    assert response.status_code == 404

def test_get_single_item():
    # Create item
    create_response = client.post(
        BASE_URL,
        json={"name": "Test Item", "description": "Test Desc"},
        headers=HEADERS
    )
    assert create_response.status_code == 201
    item_id = create_response.json()["id"]

    # Fetch it back
    get_response = client.get(f"{BASE_URL}/{item_id}", headers=HEADERS)
    assert get_response.status_code == 200
    assert get_response.json()["id"] == item_id