from sqlalchemy import select, update, delete
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
    users = self.db.execute(statement).scalars().all()
    return users 
  
  def get_user_by_email(self, user_email: str) -> schemas.User:
    return self.db.query(models.User).filter(models.User.email == user_email).first()

  def update(self, email: str, user = schemas.User):
    update_statement = update(models.User).where(
      models.User.email == email
    ).values(
      password=user.password
    )
    self.db.execute(update_statement)
    self.db.commit()
  
  def remove(self, email: str):
    delete_statement = delete(models.User).where(
      models.User.email == email
    )

    self.db.execute(delete_statement)
    self.db.commit()