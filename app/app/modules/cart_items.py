from typing import TYPE_CHECKING
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import Base


if TYPE_CHECKING:
    from . import Cart, Product


class CartItems(Base):
    __tablename__ = 'cart_items'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    cart_id: Mapped[int] = mapped_column(Integer(), ForeignKey('carts.id'))
    product_id: Mapped[int] = mapped_column(Integer(), ForeignKey('products.id'))
    count: Mapped[int] = mapped_column(Integer())
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    cart: Mapped['Cart'] = relationship(back_populates='cart_items')
    product: Mapped['Product'] = relationship(back_populates='cart_items')