from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Course
class Course(BaseModel):
  course_name: str

# Discipline
class Discipline(BaseModel):
  id: Optional[str] = None
  discipline_code: str 
  discipline_name: str 
  discipline_class: str
  discipline_course: List[Course]

# User
class User(BaseModel):
  id: Optional[str] = None
  email: EmailStr
  password: str
  user_disciplines: List[Discipline]