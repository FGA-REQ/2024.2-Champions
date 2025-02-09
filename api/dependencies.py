from fastapi import Depends, HTTPException, status, Cookie
from sqlalchemy.orm import Session
from api.infra.sqlalchemy.config.db import get_db
from api.infra.sqlalchemy.repositories.user import UserRepository

def get_current_user(user_email: str = Cookie(None), db: Session = Depends(get_db)):
    if not user_email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado (cookie não fornecido)"
        )
    user = UserRepository(db).get_user_by_email(user_email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado (usuário não encontrado)"
        )
    return user
