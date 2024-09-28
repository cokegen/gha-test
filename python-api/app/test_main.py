"""This is the main testing file"""

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    """This tests the main message"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World 5"}
