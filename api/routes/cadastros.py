from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.schemas.schemas import User, UserCreate
from api.infra.sqlalchemy.repositories.user import UserRepository
from api.infra.sqlalchemy.config.db import get_db
from pydantic import BaseModel

router = APIRouter(
  prefix="/cadastros",
  tags=["Cadastro Routes"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def cadastro(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado!")

    new_user = repo.create(User(email=user.email, password=user.password))
    return {"message": "Usuário cadastrado com sucesso!", "user": new_user.email}
