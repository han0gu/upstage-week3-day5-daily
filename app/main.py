from fastapi import FastAPI
from app.routers import todos
from app.database.connection import init_db

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """애플리케이션 시작 시 데이터베이스 테이블 생성"""
    init_db()


app.include_router(todos.router)
