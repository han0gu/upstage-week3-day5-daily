from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from app.models.todo_orm import Base

import logging

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
    """데이터베이스 테이블 생성 (이미 존재하는 경우 무시)"""
    try:
        # checkfirst=True는 기본값이지만 명시적으로 설정
        # 이미 테이블이 존재하면 아무 작업도 하지 않음
        Base.metadata.create_all(bind=engine, checkfirst=True)
    except Exception as e:
        # 테이블 생성 중 오류가 발생해도 앱 시작을 막지 않음
        # 로깅은 필요시 추가 가능
        logging.info(f"데이터베이스 테이블 생성 중 오류 발생 (무시됨): {e}")
