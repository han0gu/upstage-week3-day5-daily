import mysql.connector
from typing import List, Optional, Tuple


class TodoRepository:
    def __init__(self, conn: mysql.connector.MySQLConnection):
        self.conn = conn

    def create(self, content: str) -> int:
        """Todo 생성하고 ID 반환"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO todo (content) VALUES (%s)",
                (content,)
            )
            self.conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()

    def find_by_id(self, todo_id: int) -> Optional[Tuple]:
        """ID로 Todo 조회"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "SELECT * FROM todo WHERE id = %s",
                (todo_id,)
            )
            return cursor.fetchone()
        finally:
            cursor.close()

    def find_all(self) -> List[Tuple]:
        """모든 Todo 조회"""
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM todo")
            return cursor.fetchall()
        finally:
            cursor.close()

    def delete(self, todo_id: int) -> int:
        """Todo 삭제하고 영향받은 행 수 반환"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "DELETE FROM todo WHERE id = %s",
                (todo_id,)
            )
            self.conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
