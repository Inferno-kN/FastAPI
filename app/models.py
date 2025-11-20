from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Url(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(30))
    original_url: Mapped[str] = mapped_column(String(255))


class ClickLog(Base):
    __tablename__ = "clicks"

    id: Mapped[int] = mapped_column(primary_key=True)
    url_id: Mapped[str] = mapped_column(ForeignKey('urls.id'))
    clicked_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    user_ip: Mapped[str] = mapped_column(String(30))
    user_gadget: Mapped[str] = mapped_column(String(255))
