from sqlalchemy.orm import Session
from models import Book


def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book_title: str, book_author: str):
    new_book = Book(title=book_title, author=book_author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update_book(db: Session, book_id: int, new_title: str, new_author: str):
    book = get_book(db, book_id)
    if book:
        book.title = new_title
        book.author = new_author
        db.commit()
        db.refresh(book)
        return book
    return None

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False