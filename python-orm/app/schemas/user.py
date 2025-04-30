from pydantic import BaseModel

# 유저 스키마
# 유저의 기본 정보를 담고 있는 스키마
class UserBase(BaseModel):
    username: str
    email: str

# 유저 생성
# 유저 생성시 username과 email을 받음
# UserCreate는 UserBase를 상속받아서 pass
class UserCreate(UserBase):
    pass

# 유저 업데이트
class User(UserBase):
        id: int

        class Config:
            from_attributes = True