from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from app.models.todo_orm import Base

# 데이터베이스 URL
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/test_db"

# Engine 생성
engine = create_engine(DATABASE_URL, echo=False)

# SessionLocal 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """데이터베이스 세션 생성"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """데이터베이스 테이블 생성 (선택사항)"""
    Base.metadata.create_all(bind=engine)
