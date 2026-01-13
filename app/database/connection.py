import mysql.connector
from typing import Generator


def get_db() -> Generator:
    """데이터베이스 연결 생성"""
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="test_db",
    )
    try:
        yield conn
    finally:
        conn.close()
