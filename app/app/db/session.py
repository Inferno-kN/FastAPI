from sqlalchemy import create_engine
from app.modules.base import Base


db_path = "sqlite:///app/db/shop.db"
engine = create_engine(db_path, echo=True)


def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)