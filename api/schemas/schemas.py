from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Course
class Course(BaseModel):
    course_name: str

    class Config:
        orm_mode = True

# Discipline
class Discipline(BaseModel):
    discipline_code: str 
    discipline_name: str 
    users: Optional[List["UserSimple"]] = []

    class Config:
        orm_mode = True

# User
class User(BaseModel):
    email: EmailStr
    password: str
    disciplines: Optional[List[Discipline]] = []

    class Config:
        orm_mode = True

class UserSimple(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Login 
class LoginData(BaseModel):
    email: EmailStr
    password: str
