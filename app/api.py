from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.models import Url
from app.utils import log_click
from app.db import create_db_and_tables
from fastapi.responses import RedirectResponse
from fastapi import HTTPException

router = APIRouter()

@router.get("/{code}", response_class=RedirectResponse)
def redirect(code: str, request: Request, db: Session = Depends(create_db_and_tables)):
    url = db.query(Url).filter_by(code=code).first()
    if url is None:
        raise HTTPException(status_code=404, detail="Страница не найдена")

    log_click(url.id, request.client.host, request.headers.get("User-Agent"))
    return RedirectResponse(url.original_url)