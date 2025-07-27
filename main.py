from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from Models.Book import Book
import os

books_db = [
    {
        "id": 0,
        "title": "Harry Potter",
        "year": "2009",
        "score": 5
    },
    {
        "id": 1,
        "title": "Bridget Jhones Diary",
        "year": "1990",
        "score": 5
    },
    {
        "id": 2,
        "title": "Las Mil y Una Noches",
        "year": "2005",
        "score": 4
    },
    {
        "id": 3,
        "title": "The Lord Rings",
        "year": "2003",
        "score": 3
    },
    {
        "id": 4,
        "title": "The Hobbit",
        "year": "2004",
        "score": 2
    }
]

origins = [
    "http://localhost:5173"
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")  # decorator
def root():
    return {"message": "Hello World"}


@app.get("/api/v1/books", response_model=list[Book])  # decorator
def get_books():
    return books_db


@app.get("/api/v1/books/{book_id}", response_model=Book)  # decorator
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with id {book_id} not found")


@app.post("/api/v1/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: Book):  # book:Book is a model
    new_book = book_data.dict()
    books_db.append(new_book)
    return new_book


@app.delete("/api/v1/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            books_db.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with id {book_id} not found")


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
