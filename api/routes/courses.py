from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api.schemas.schemas import Course
from api.infra.sqlalchemy.repositories.course import CourseRepository
from api.infra.sqlalchemy.config.db import get_db

router = APIRouter(
  prefix='/courses',
  tags=['Courses Routes']
)

@router.get("/")
def get_courses():
  return { "Message": "Hello from Courses Router!"}

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_course(course: Course, db: Session = Depends(get_db)):
  course_created = CourseRepository(db).create(course)
  return course_created