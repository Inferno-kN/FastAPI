from app.models import ClickLog
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from app.db import engine


Session = sessionmaker(engine)


def log_click(url_id, user_ip, user_gadget):
    with Session() as session:
        try:
            new_log = ClickLog(url_id=url_id, user_ip=user_ip, user_gadget=user_gadget, clicked_at=datetime.now())
            session.add(new_log)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e