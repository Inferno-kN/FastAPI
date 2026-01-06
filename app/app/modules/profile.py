from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List, TYPE_CHECKING
from .base import Base


if TYPE_CHECKING:
    from .review import Review
    from .order import Order
    from .cart import Cart


class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(45))
    surname: Mapped[str] = mapped_column(String(45))
    phone: Mapped[str] = mapped_column(String(45))
    birthday: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())
    photo: Mapped[str] = mapped_column(String(45))
    user_id: Mapped[int] = mapped_column(Integer(), ForeignKey("users.id"))

    cart: Mapped['Cart'] = relationship('Cart', back_populates='profile')
    reviews: Mapped[List['Review']] = relationship('Review', back_populates='profile')
    orders: Mapped[List['Order']] = relationship('Order', back_populates='profile')