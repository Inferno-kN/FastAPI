from app.modules.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime, ForeignKey
from datetime import datetime
from typing import List, TYPE_CHECKING


if TYPE_CHECKING:
    from . import CartItems, Profile


class Cart(Base):
    __tablename__ = 'carts'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())
    profile_id: Mapped[int] = mapped_column(Integer(), ForeignKey('profiles.id'))

    cart_items: Mapped[List['CartItems']] = relationship(back_populates='cart')
    profile: Mapped['Profile'] = relationship('Profile', back_populates='cart')