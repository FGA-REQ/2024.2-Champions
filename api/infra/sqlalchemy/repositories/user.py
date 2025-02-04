from sqlalchemy import select
from sqlalchemy.orm import Session
from api.schemas import schemas
from api.infra.sqlalchemy.models import models

class UserRepository():
  def __init__(self, db: Session):
    self.db = db 
  
  def create(self, course: schemas.User):
    db_user = models.User(
      email = course.email,
      password = course.password
    )
    self.db.add(db_user)
    self.db.commit()
    self.db.refresh(db_user)
    return db_user
  
  def list_all(self):
    statement = select(models.User)
    users = self.db.execute(statement).all()
    return users 
  
  def get(self):
    ... 
  
  def remove(self):
    ...