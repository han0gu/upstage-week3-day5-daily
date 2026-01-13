from fastapi import HTTPException
from typing import List
import mysql.connector
from app.repositories.todo_repository import TodoRepository
from app.models.todo import TodoCreate, TodoResponse


class TodoService:
    def __init__(self, conn: mysql.connector.MySQLConnection):
        self.repository = TodoRepository(conn)

    def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
        """Todo 생성"""
        if not todo_data.content:
            raise HTTPException(status_code=400, detail="content is required")

        todo_id = self.repository.create(todo_data.content)
        row = self.repository.find_by_id(todo_id)

        if not row:
            raise HTTPException(status_code=500, detail="Failed to create todo")

        return TodoResponse(
            id=row[0],
            content=row[1],
            created_at=row[2]
        )

    def get_all_todos(self) -> List[TodoResponse]:
        """모든 Todo 조회"""
        rows = self.repository.find_all()
        return [
            TodoResponse(
                id=r[0],
                content=r[1],
                created_at=r[2]
            )
            for r in rows
        ]

    def delete_todo(self, todo_id: int) -> dict:
        """Todo 삭제"""
        affected = self.repository.delete(todo_id)

        if affected == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

        return {"message": "Todo deleted"}
