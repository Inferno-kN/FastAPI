from fastapi import FastAPI
from api import router
from db import engine, create_db_and_tables

app = FastAPI()

@app.get("start")
def start_event():
    create_db_and_tables()

app.include_router(router)