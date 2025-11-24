import crud, schemas
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal

router = APIRouter()

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books")
async def list_books(db: Session = Depends(get_database)):
    books = crud.get_books(db)
    return books

@router.get("/books/{book_id}")
async def return_book(book_id: int, db: Session = Depends(get_database)):
    book = crud.get_book(db, book_id)
    return book

@router.post("/books")
async def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_database)):
    new_book = crud.create_book(db=db, book_title=book.title, book_author=book.author)
    return new_book

@router.put("/books/{book_id}")
async def update_new_book(book_id: int, update_data: schemas.BookUpdate, db: Session = Depends(get_database)):
    updated_book = crud.update_book(db=db, book_id=book_id, new_title=update_data.title, new_author=update_data.author)
    return updated_book

@router.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_database)):
    deleted_book = crud.delete_book(db=db, book_id=book_id)
    return {"message": "Книга успешно удалена."}