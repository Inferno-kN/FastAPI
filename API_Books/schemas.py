from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str

    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title: str
    author: str  # Эти поля обязательны при создании книги

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None