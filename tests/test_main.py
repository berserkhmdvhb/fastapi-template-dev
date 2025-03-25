from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_404():
    """Test that root path is not defined and returns 404"""
    response = client.get("/")
    assert response.status_code == 404

def test_docs_available():
    """Swagger UI should be available"""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_redoc_available():
    """ReDoc docs should be available"""
    response = client.get("/redoc")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_invalid_path():
    """Invalid endpoint returns 404"""
    response = client.get("/this/does/not/exist")
    assert response.status_code == 404
