from fastapi import APIRouter, status, Depends, Form
from api.infra.sqlalchemy.config.db import get_db
from api.infra.sqlalchemy.repositories.user import UserRepository
from api.schemas.schemas import User
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
  prefix='/users',
  tags=['User Routes']
)

# @router.get("/", status_code=status.HTTP_200_OK)
# def get():
#   return {'msg' : "Hello from Users Router!"}

# Return all users
@router.get("/", response_model=List[User])
def list_users(db: Session = Depends(get_db)):
  users = UserRepository(db).list_all()
  return users

# Return a user by email
@router.get('/{email}')
def get_by_email(email: str, db: Session = Depends(get_db)):
  user = UserRepository(db).get_user_by_email(email)
  return user

# Create a user
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user: User, db: Session = Depends(get_db)):
  user_created = UserRepository(db).create(user)
  return user_created

# Update a user`s password 
@router.put('/')
def update_password(email:str, user: User, db: Session = Depends(get_db)):
  user_updated = UserRepository(db).update(email, user)
  return user_updated

@router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
  return UserRepository(db).remove(email)