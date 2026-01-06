from typing import TYPE_CHECKING

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey


if TYPE_CHECKING:
    from . import Order


class OrderItems(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    order_id: Mapped[int] = mapped_column(Integer(), ForeignKey('orders.id'))
    quantity: Mapped[int] = mapped_column(Integer())
    price: Mapped[int] = mapped_column(Integer())
    cost: Mapped[int] = mapped_column(Integer())
    product_id: Mapped[int] = mapped_column(Integer(), ForeignKey('products.id'))

    order: Mapped['Order'] = relationship(back_populates='order_items')