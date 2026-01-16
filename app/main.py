from fastapi import FastAPI
from app.routers import todos
from app.database.connection import init_db
from app.config.logging import setup_logging

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """애플리케이션 시작 시 초기화 작업 수행"""
    # 로깅 설정 초기화
    setup_logging()

    # 데이터베이스 테이블 생성
    init_db()


app.include_router(todos.router)
