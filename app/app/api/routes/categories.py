from fastapi import APIRouter


router = APIRouter(prefix="/category", tags=["categories"])


@router.get("", summary='Получение категорий')
async def get_categories():
    return []


