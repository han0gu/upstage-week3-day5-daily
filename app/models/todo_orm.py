from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class TodoORM(Base):
    """SQLAlchemy ORM 모델"""
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
