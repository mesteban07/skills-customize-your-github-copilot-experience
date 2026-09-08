# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice HTTP methods, route parameters, request validation, and JSON responses. By the end of the assignment, you will have an interactive API that can manage a collection of books.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Set up the FastAPI application and add an endpoint that confirms the API is running.

#### Requirements

Completed program should:

- Create a `FastAPI` application in `starter-code.py`.
- Add a `GET /` endpoint.
- Return a JSON response with a message confirming that the API is running.
- Start the development server with Uvicorn and verify the endpoint in the browser or API documentation.

### 🛠️ Add Book Endpoints

#### Description

Create endpoints that let clients view the available books and add a new book to the collection.

#### Requirements

Completed program should:

- Store books as a list of dictionaries with an `id`, `title`, and `author`.
- Add a `GET /books` endpoint that returns all books as JSON.
- Add a `POST /books` endpoint that accepts a JSON book with `title` and `author`.
- Assign a unique ID to each new book and return the created book.
- Return an appropriate HTTP status code for a successful book creation.

### 🛠️ Validate and Update Books

#### Description

Use Pydantic models and route parameters to validate book data and update an existing book.

#### Requirements

Completed program should:

- Define a Pydantic model for incoming book data.
- Reject requests that omit `title` or `author` with FastAPI validation errors.
- Add a `PUT /books/{book_id}` endpoint that updates an existing book.
- Return a clear `404` response when the requested book does not exist.
- Test the endpoints using the automatically generated documentation at `/docs`.
