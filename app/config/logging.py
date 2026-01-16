import logging
from logging.handlers import RotatingFileHandler
import os

# ---------------------------
# [TASK 1] 로그 저장 폴더 생성
# ---------------------------
# TODO: "logs"라는 이름의 폴더를 생성해주세요!
# Hint: os.makedirs()를 활용하면 됩니다. 이미 폴더가 있어도 에러가 나지 않도록 exist_ok=True 옵션 사용
log_file_dir = "logs"
os.makedirs(log_file_dir, exist_ok=True)

# ---------------------------
# [TASK 2] 로그 포맷 및 핸들러 설정
# ---------------------------
# TODO: LOG_FORMAT을 사용하여 formatter를 생성하세요
# Hint: logging.Formatter()를 사용하여 LOG_FORMAT을 전달
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
log_formatter = logging.Formatter(LOG_FORMAT)

# ---------------------------
# [TASK 2-1] file handler 설정
# ---------------------------
file_handler = RotatingFileHandler(
    # TODO: 로그 파일 경로를 지정하세요 (logs 폴더 안에 app.log 파일)
    # Hint: "logs/파일명.확장자" 형식으로 작성
    filename=f"{log_file_dir}/app.log",
    # TODO: 로그 파일의 최대 크기를 바이트 단위로 지정하세요
    # Hint: 1MB = 1024 * 1024 바이트
    maxBytes=1024 * 1024,
    # TODO: 보관할 백업 파일 개수를 지정하세요
    # Hint: 5개의 백업 파일을 유지하려면?
    backupCount=5,
    encoding="utf-8",
)
file_handler.setFormatter(log_formatter)

# ---------------------------
# [TASK 2-2] console handler 설정
# ---------------------------
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

# ---------------------------
# [TASK 3] 루트 로거 통합 설정
# ---------------------------
# TODO: 로그 레벨을 INFO로 설정하세요
# Hint: logging 모듈의 INFO 상수를 사용하세요
root_logger = logging.getLogger()
root_logger.setLevel("INFO")  # 이 부분을 채워주세요!

# TODO: 파일 핸들러를 루트 로거에 추가하세요
# Hint: addHandler() 메서드를 사용하여 file_handler를 추가
root_logger.addHandler(file_handler)

# TODO: 콘솔 핸들러를 루트 로거에 추가하세요
# Hint: addHandler() 메서드를 사용하여 console_handler를 추가
root_logger.addHandler(console_handler)


def setup_logging():
    """로깅 설정을 초기화하는 함수"""
    # uvicorn 로거도 동일한 핸들러 사용
    logging.getLogger("uvicorn").handlers = root_logger.handlers
    logging.getLogger("uvicorn.access").handlers = root_logger.handlers
