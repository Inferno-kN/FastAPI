import enum
from typing import TYPE_CHECKING
from sqlalchemy import String, Enum, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .base import Base


if TYPE_CHECKING:
    from . import Profile


class UserStatus(enum.Enum):
    admin = 'admin'
    moderator = 'moderator'


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(45), unique=True)
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), nullable=False, default=UserStatus.admin)
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now(), onupdate=datetime.now())
    profile: Mapped["Profile"] = relationship('Profile', back_populates='user_id')
