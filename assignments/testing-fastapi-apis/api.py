from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


class BookInput(BaseModel):
    title: str
    author: str


@app.get("/")
def read_root():
    return {"message": "Book API is running"}


@app.get("/books")
def list_books():
    return books


@app.post("/books", status_code=201)
def create_book(book: BookInput):
    new_book = {"id": max(item["id"] for item in books) + 1, **book.model_dump()}
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    for index, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            updated_book = {"id": book_id, **book.model_dump()}
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")
