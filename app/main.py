from fastapi import FastAPI, HTTPException, status
from typing import List
from app.schemas import BookCreate, BookResponse, BookUpdate

from DAL.data_layer import (create_book as dal_create_book,delete_book as dal_delete_book,get_book as dal_get_book,get_books as dal_get_books,update_book as dal_update_book,)

app = FastAPI(title="Book Management API",version="1.0.0")

@app.get("/books",response_model=List[BookResponse],status_code=status.HTTP_200_OK)
def get_all_books():
    return dal_get_books()


@app.get("/books/{book_id}",response_model=BookResponse,status_code=status.HTTP_200_OK)
def read_single_book(book_id: int):
    book = dal_get_book(book_id)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    return book

@app.post("/books",response_model=BookResponse,status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate):
    return dal_create_book(payload.model_dump())


@app.put("/books/{book_id}",response_model=BookResponse)
def update_book(book_id: int, payload: BookUpdate):
    book = dal_get_book(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    updated_book = book.copy()
    if payload.title is not None:
        updated_book["title"] = payload.title

    if payload.author is not None:
        updated_book["author"] = payload.author

    if payload.isbn is not None:
        updated_book["isbn"] = payload.isbn

    if payload.published_year is not None:
        updated_book["published_year"] = payload.published_year

    if payload.genre is not None:
        updated_book["genre"] = payload.genre

    if payload.available is not None:
        updated_book["available"] = payload.available


    return dal_update_book(book_id, updated_book)

@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(book_id: int):
    book = dal_get_book(book_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    dal_delete_book(book_id)