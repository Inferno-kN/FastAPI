from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import List, TYPE_CHECKING


if TYPE_CHECKING:
    from . import CartItems, Review, CategoriesHasProducts


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(45))
    article: Mapped[str] = mapped_column(String(45), unique=True)
    preview_text: Mapped[str] = mapped_column(Text())
    detail_text: Mapped[str] = mapped_column(Text())
    price: Mapped[int] = mapped_column(Integer())

    cart_items: Mapped[List['CartItems']] = relationship('CartItems', back_populates='product')
    reviews: Mapped[List['Review']] = relationship('Review', back_populates='product')
    categories_has_products3: Mapped[List['CategoriesHasProducts']] = relationship(back_populates='product')
