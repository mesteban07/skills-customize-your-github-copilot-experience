# 📘 Assignment: Testing FastAPI APIs with Pytest

## 🎯 Objective

Write an automated test suite for a FastAPI book API using Pytest and FastAPI's test client. You will practice testing successful responses, validation failures, missing resources, and test isolation.

## 📝 Tasks

### 🛠️ Test Successful API Requests

#### Description

Use `TestClient` to verify that the API responds correctly for its health check and book-listing endpoints.

#### Requirements

Completed test suite should:

- Create a reusable `TestClient` for the FastAPI application.
- Test that `GET /` returns a `200` status code and the expected status message.
- Test that `GET /books` returns a `200` status code and a JSON list.
- Verify that each returned book includes an `id`, `title`, and `author`.

### 🛠️ Test Book Creation and Updates

#### Description

Test the API's write operations with valid request bodies and confirm that the response contains the expected book data.

#### Requirements

Completed test suite should:

- Test that `POST /books` creates a book and returns a `201` status code.
- Verify that the created book includes a unique integer ID and the submitted title and author.
- Test that `PUT /books/{book_id}` updates an existing book.
- Confirm that the updated response contains the changed title and author.

### 🛠️ Test Errors and Isolated State

#### Description

Add negative tests and fixtures that keep tests reliable when they run individually or in a different order.

#### Requirements

Completed test suite should:

- Test that a book request missing `title` or `author` returns a `422` validation response.
- Test that updating a nonexistent book returns a `404` response.
- Use a fixture or setup step to prevent one test's created data from affecting another test.
- Run the full suite with `pytest` and achieve a passing result.
