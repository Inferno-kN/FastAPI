from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


if TYPE_CHECKING:
    from . import Profile, Product


class Review(Base):
    __tablename__ = 'reviews'

    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    rate: Mapped[int] = mapped_column(Integer())

    profile: Mapped['Profile'] = relationship(back_populates='reviews')
    product: Mapped['Product'] = relationship(back_populates='reviews')