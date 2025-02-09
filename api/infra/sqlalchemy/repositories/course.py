from sqlalchemy.orm import Session
from api.schemas import schemas
from api.infra.sqlalchemy.models import models

class CourseRepository():
    def __init__(self, db: Session):
        self.db = db

    def create(self, course: schemas.Course):
        db_course = models.Course(
            course_name=course.course_name
        )
        self.db.add(db_course)
        self.db.commit()
        self.db.refresh(db_course)
        return db_course

    def list_all(self):
        courses = self.db.query(models.Course).all()
        return courses

    def get(self):
        pass

    def remove(self):
        pass
