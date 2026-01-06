from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


if TYPE_CHECKING:
    from . import Product, Category


class CategoriesHasProducts(Base):
    __tablename__ = 'categories_has_products'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    categories_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    products_id: Mapped[int] = mapped_column(ForeignKey('products.id'))

    category: Mapped['Category'] = relationship(back_populates='categories_has_products2')
    product: Mapped['Product'] = relationship(back_populates='categories_has_products3')