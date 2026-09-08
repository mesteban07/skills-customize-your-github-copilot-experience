import pytest
from fastapi.testclient import TestClient

from api import app, books


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_books():
    original_books = [book.copy() for book in books]
    yield
    books.clear()
    books.extend(original_books)


def test_health_check(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Book API is running"


# Add tests for listing books, creating and updating books, validation errors,
# and requests for missing books.
