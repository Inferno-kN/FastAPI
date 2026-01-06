from fastapi import APIRouter


router = APIRouter(prefix="/products", tags=["products"])


@router.get("", summary='Получение продуктов')
async def get_products():
    return []


