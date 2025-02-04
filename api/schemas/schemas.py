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
  # discipline_course: List[Course]

  class Config:
    orm_mode = True

# User
class User(BaseModel):
  email: EmailStr
  password: str
  # user_disciplines: List[Discipline]

  class Config:
    orm_mode = True