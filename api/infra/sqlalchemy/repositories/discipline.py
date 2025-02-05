from sqlalchemy.orm import Session
from sqlalchemy import delete, insert
from api.schemas import schemas
from api.infra.sqlalchemy.models import models

class DisciplineRepository():
    def __init__(self, db: Session):
        self.db = db 
      
    def create(self, discipline: schemas.Discipline):
        db_discipline = models.Discipline(
            discipline_code = discipline.discipline_code,
            discipline_name = discipline.discipline_name
        )
        self.db.add(db_discipline)
        self.db.commit()
        self.db.refresh(db_discipline)
        return db_discipline
      
    def list_all(self):
        disciplines = self.db.query(models.Discipline).all()
        return disciplines

    def add_user_to_discipline(self, user_email: str, discipline_code: str):
        """Vincula um usuário à disciplina usando a tabela associativa."""
        stmt = insert(models.user_discipline).values(
            user_email=user_email, 
            discipline_code=discipline_code
        )
        self.db.execute(stmt)
        self.db.commit()

    def remove(self, discipline_code: str):
        delete_statement = delete(models.Discipline).where(
            models.Discipline.discipline_code == discipline_code
        )
        self.db.execute(delete_statement)
        self.db.commit()
