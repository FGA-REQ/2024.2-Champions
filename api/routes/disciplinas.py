from fastapi import APIRouter, Depends, status
from api.infra.sqlalchemy.config.db import get_db
from api.schemas.schemas import Discipline
from sqlalchemy.orm import Session
from api.infra.sqlalchemy.repositories.discipline import DisciplineRepository
router = APIRouter(
    prefix = "/disciplinas",
    tags = ["Rotas de Disciplina"] 
)

@router.get("/", status_code = status.HTTP_200_OK)
def get_disciplines(db: Session = Depends(get_db)):
    disciplinas = DisciplineRepository(db).list_all()
    return disciplinas
    

#@router.post('/', status_code=status.HTTP_201_CREATED)
#def create_user(user: User, db: Session = Depends(get_db)):
#user_created = UserRepository(db).create(user)
 # return user_created
 
@router.post("/")
def create_disciplinas(discipline: Discipline, db: Session = Depends(get_db)):
    disciplina_criated = DisciplineRepository(db).create(discipline)
    return disciplina_criated

@router.delete("/{discipline_code}", status_code=status.HTTP_204_NO_CONTENT)
def delete(discipline_code:str, db: Session = Depends(get_db)):
  return DisciplineRepository(db).remove(discipline_code)
    