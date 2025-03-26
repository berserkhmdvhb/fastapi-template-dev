from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """
    Root path test.
    If no route is defined at '/', it should return 404.
    If later defined, update this to match expected response.
    """
    response = client.get("/")
    assert response.status_code == 404  # Change this if you add a root route

def test_docs_available():
    """Swagger UI (/docs) should be available and return HTML."""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_redoc_available():
    """ReDoc documentation (/redoc) should be available and return HTML."""
    response = client.get("/redoc")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_invalid_path():
    """Nonexistent endpoint should return 404."""
    response = client.get("/this/does/not/exist")
    assert response.status_code == 404