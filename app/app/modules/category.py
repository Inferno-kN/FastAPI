from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from .base import Base


if TYPE_CHECKING:
    from . import CategoriesHasProducts


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey('categories.categories_id'))
    photo: Mapped[str] = mapped_column(String(255))
    sort: Mapped[int] = mapped_column(Integer())

    categories_has_products2: Mapped[List['CategoriesHasProducts']] = relationship(back_populates='category')