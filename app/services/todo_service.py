from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository
from app.models.todo import TodoCreate, TodoResponse

import logging


class TodoService:
    def __init__(self, db: Session):
        self.repository = TodoRepository(db)

    def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
        """Todo 생성"""
        if not todo_data.content:
            # TODO: ERROR 레벨로 로그를 기록하세요
            # Hint: logging.error()를 사용하여 "제목이 없는 할 일 생성 시도: content missing" 메시지 기록
            logging.error("제목이 없는 할 일 생성 시도: content missing")

            raise HTTPException(status_code=400, detail="content is required")

        todo = self.repository.create(todo_data.content)

        # TODO: INFO 레벨로 로그를 기록하세요
        # Hint: logging.info()를 사용하여 "새로운 할 일 생성 완료: ID {todo_id}" 메시지 기록 (f-string 사용)
        logging.info(f"새로운 할 일 생성 완료: ID {todo.id}")

        return TodoResponse(
            id=todo.id, content=todo.content, created_at=todo.created_at
        )

    def get_all_todos(self) -> List[TodoResponse]:
        """모든 Todo 조회"""
        todos = self.repository.find_all()
        return [
            TodoResponse(id=todo.id, content=todo.content, created_at=todo.created_at)
            for todo in todos
        ]

    def delete_todo(self, todo_id: int) -> dict:
        """Todo 삭제"""
        affected = self.repository.delete(todo_id)

        if affected == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

        return {"message": "Todo deleted"}
