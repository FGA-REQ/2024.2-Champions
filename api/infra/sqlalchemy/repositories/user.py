from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from api.schemas import schemas
from api.infra.sqlalchemy.models import models

class UserRepository():
    def __init__(self, db: Session):
        self.db = db 
      
    def create(self, user: schemas.User):
        db_user = models.User(
            email=user.email,
            password=user.password
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
  
    def create_user(self, new_email: str, new_password: str):
        user = models.User(email=new_email, password=new_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
  
    def list_all(self):
        statement = select(models.User)
        users = self.db.execute(statement).scalars().all()
        return users 
  
    def get_user_by_email(self, user_email: str) -> schemas.User:
        return self.db.query(models.User).filter(models.User.email == user_email).first()
  
    def update(self, email: str, user: schemas.User):
        update_statement = update(models.User).where(
            models.User.email == email
        ).values(
            password=user.password
        )
        self.db.execute(update_statement)
        self.db.commit()

    def update_password(self, email: str, new_password: str):
        user = self.db.query(models.User).filter(models.User.email == email).first()
        if not user: 
            return
        update_statement = update(models.User).where(
            models.User.email == email
        ).values(
            password=new_password
        )
        self.db.execute(update_statement)
        self.db.commit()
        updated_user = self.db.query(models.User).filter(models.User.email == email).first()
        return updated_user

    def remove(self, email: str):
        delete_statement = delete(models.User).where(
            models.User.email == email
        )
        self.db.execute(delete_statement)
        self.db.commit()
