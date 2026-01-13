from typing import List
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.services.todo_service import TodoService
from app.models.todo import TodoCreate, TodoResponse
from app.database.connection import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


def get_todo_service(db: Session = Depends(get_db)) -> TodoService:
    """TodoService 의존성 주입"""
    return TodoService(db)


@router.post("", response_model=TodoResponse)
async def create_todo(
    request: Request, service: TodoService = Depends(get_todo_service)
):
    """Todo 생성"""
    body = await request.json()
    todo_data = TodoCreate(**body)
    return service.create_todo(todo_data)


@router.get("", response_model=List[TodoResponse])
def get_todos(service: TodoService = Depends(get_todo_service)):
    """모든 Todo 조회"""
    return service.get_all_todos()


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    """Todo 삭제"""
    return service.delete_todo(todo_id)
