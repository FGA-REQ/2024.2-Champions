from fastapi import APIRouter, status, Depends, Form, HTTPException
from api.infra.sqlalchemy.config.db import get_db
from api.infra.sqlalchemy.repositories.user import UserRepository
from api.schemas.schemas import User, LoginData
from sqlalchemy.orm import Session
from api.infra.providers import hash_provider
from typing import List
from fastapi.templating import Jinja2Templates

#AQUI ACONTECE A AUTENTICACAO DE USUARIO

router = APIRouter(
  prefix='/auth',
  tags=['User Routes']
)

templates = Jinja2Templates(directory='templates')

# Return all users
@router.get("/", response_model=List[User])
def list_users(db: Session = Depends(get_db)):
  users = UserRepository(db).list_all()
  return users

# Return a user by email
@router.get('/{email}')
def get_by_email(email: str, db: Session = Depends(get_db)):
  user = UserRepository(db).get_user_by_email(email)
  if not user:
      raise HTTPException(status_code=404, detail='Usuario nao encontrado.')
  return user

# Create a user (SIGN UP)
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user: User, db: Session = Depends(get_db)):
  user_loc = UserRepository(db).get_user_by_email(user.email)

  if user_loc:
    raise HTTPException(status_code=404, detail="Usuario ja existente.")

  user.password = hash_provider.generate_hash(user.password)
  user_created = UserRepository(db).create(user)
  return user_created

# Update a user`s password 
@router.put('/')
def update_password(email:str, user: User, db: Session = Depends(get_db)):
  user_updated = UserRepository(db).update(email, user)
  return user_updated

# Delete route
@router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
  return UserRepository(db).remove(email)

# Login route
@router.post('/login')
def login(login_data: LoginData, db: Session = Depends(get_db)):
  psswrd = login_data.password
  email = login_data.email

  user = UserRepository(db).get_user_by_email(email)

  if not user:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email ou senha incorretos!')
  
  valid_password = hash_provider.verify_hash(psswrd, user.password)

  if not valid_password:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Senha incorreta!')
  
  return user