from sqlalchemy import create_engine
from app.models  import Base


db_path = "sqlite:///./shortened_urls.db"

engine = create_engine(db_path, echo=True)

def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)