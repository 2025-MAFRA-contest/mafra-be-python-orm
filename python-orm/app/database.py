from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB연결
# SQLite를 사용하여 데이터베이스 연결을 설정

# test.db라는 파일 생성(데이터베이스)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


# SQLAlchemy라는 DB연결 엔진 생성 및 연결
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 세션 클래스 생성(DB와 연결된 세션을 생성하는 클래스)
# SQL문 실행을 위한 세션을 생성하는 클래스
# autocommit-> 자동 커밋 여부, autoflush-> 자동으로 flush할지 여부
# flush-> DB에 쿼리문을 날려서 DB에 반영하는 것
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델(엔티티) 클래스가 상속받을 BASE 클래스 선언
# ORM 모델 클래스들은 이걸 상속받아야함
# 이걸 상속받아야 SQLAlchemy가 테이블로 인식
Base = declarative_base()