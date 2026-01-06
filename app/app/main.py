from fastapi import FastAPI, APIRouter
from app.api.routes.categories import router as category_router
from app.api.routes.products import router as product_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(category_router)
    app.include_router(product_router)
    return app


app = create_app()