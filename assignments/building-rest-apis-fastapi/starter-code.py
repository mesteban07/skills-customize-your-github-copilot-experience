# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/")
def read_root():
    # Add a JSON response that confirms the API is running.
    pass


@app.get("/books")
def list_books():
    # Return the current collection of books.
    pass


# Add a Pydantic model and POST/PUT endpoints for the assignment.
