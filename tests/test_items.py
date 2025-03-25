from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "Just testing"},
        headers={"token": "fake-super-secret-token"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"