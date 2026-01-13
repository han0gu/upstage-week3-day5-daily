from pydantic import BaseModel
from datetime import datetime


class TodoCreate(BaseModel):
    content: str


class TodoResponse(BaseModel):
    id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
