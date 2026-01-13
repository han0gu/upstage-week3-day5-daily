from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.todo_orm import TodoORM


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, content: str) -> TodoORM:
        """Todo 생성하고 반환"""
        todo = TodoORM(content=content)
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def find_by_id(self, todo_id: int) -> Optional[TodoORM]:
        """ID로 Todo 조회"""
        return self.db.query(TodoORM).filter(TodoORM.id == todo_id).first()

    def find_all(self) -> List[TodoORM]:
        """모든 Todo 조회"""
        return self.db.query(TodoORM).all()

    def delete(self, todo_id: int) -> int:
        """Todo 삭제하고 영향받은 행 수 반환"""
        todo = self.db.query(TodoORM).filter(TodoORM.id == todo_id).first()
        if todo:
            self.db.delete(todo)
            self.db.commit()
            return 1
        return 0
