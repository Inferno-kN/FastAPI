import enum
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Enum, ForeignKey
from typing import List, TYPE_CHECKING


if TYPE_CHECKING:
    from . import Profile, OrderItems


class OrderStatus(enum.Enum):
    completed = 'completed'
    failed = 'failed'
    draft = 'draft'


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), nullable=False, default=OrderStatus.draft)
    total_price: Mapped[int] = mapped_column(Integer(), nullable=False)
    profile_id: Mapped[int] = mapped_column(Integer(), ForeignKey('profiles.id'))

    profile: Mapped['Profile'] = relationship(back_populates='orders')
    order_items: Mapped[List['OrderItems']] = relationship(back_populates='order')
