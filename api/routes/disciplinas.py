from fastapi import APIRouter, Depends, Request, status
from api.infra.sqlalchemy.config.db import get_db
from api.schemas.schemas import Discipline
from sqlalchemy.orm import Session
from api.infra.sqlalchemy.repositories.discipline import DisciplineRepository
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/disciplinas",
    tags=["Rotas de Disciplina"] 
)

templates = Jinja2Templates(directory="templates")

@router.get("/", status_code=status.HTTP_200_OK)
def ver_disciplinas(request: Request, db: Session = Depends(get_db)):
    repo = DisciplineRepository(db)
    disciplinas = repo.list_all()
    return templates.TemplateResponse("ver_disciplinas.html", {"request": request, "disciplinas": disciplinas})

@router.post("/")
def create_disciplinas(discipline: Discipline, db: Session = Depends(get_db)):
    disciplina_created = DisciplineRepository(db).create(discipline)
    return disciplina_created

@router.delete("/{discipline_code}", status_code=status.HTTP_204_NO_CONTENT)
def delete(discipline_code: str, db: Session = Depends(get_db)):
    return DisciplineRepository(db).remove(discipline_code)
