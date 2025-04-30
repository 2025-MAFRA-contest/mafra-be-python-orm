from sqlalchemy import Column, Integer, String
from app.database import Base

# DB 테이블 구조 정의
# User 모델 클래스
# users테이블의 정보를 반환할 객체
# Base클래스 상속

class User(Base):
    __tablename__ = "users"  # 테이블 이름으로 지정

    id = Column(Integer, primary_key=True, index=True)  # id는 기본키
    username = Column(String, unique=True, index=True)  # username은 유일한 값
    email = Column(String, unique=True, index=True)  # email은 유일한 값
    full_name = Column(String)  # full_name은 유일한 값