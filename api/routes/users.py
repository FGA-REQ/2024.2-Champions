from fastapi import APIRouter, status, Depends
from api.infra.sqlalchemy.config.db import get_db
from api.infra.sqlalchemy.repositories.user import UserRepository
from api.schemas.schemas import User
from sqlalchemy.orm import Session

router = APIRouter(
  prefix='/users',
  tags=['User Routes']
)

# @router.get("/", status_code=status.HTTP_200_OK)
# def get():
#   return {'msg' : "Hello from Users Router!"}

@router.get("/")
def list_users(db: Session = Depends(get_db)):
  users = UserRepository(db).list_all()
  return users

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user: User, db: Session = Depends(get_db)):
  user_created = UserRepository(db).create(user)
  return user_created