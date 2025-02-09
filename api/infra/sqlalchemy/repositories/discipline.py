from sqlalchemy.orm import Session
from sqlalchemy import delete, insert, select
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

    def search_discipline(self, search: str):
        query = self.db.query(models.Discipline)
        query = query.filter(
            (models.Discipline.discipline_code.ilike(f'%{search}%')) |  
            (models.Discipline.discipline_name.ilike(f'%{search}%'))  
        )
        return query.all()

    def add_user_to_discipline(self, user_email: str, discipline_code: str):
        """Associa um usuário à disciplina usando a tabela user_discipline,
        verificando antes se a associação já existe."""
        # Verifica se a associação já existe
        stmt_check = select(models.user_discipline).filter(
            models.user_discipline.c.user_email == user_email,
            models.user_discipline.c.discipline_code == discipline_code
        )
        result = self.db.execute(stmt_check).first()
        if result:
            # Já existe associação; retorna False para indicar que nada foi inserido
            return False

        # Se não existir, cria a associação
        stmt = insert(models.user_discipline).values(
            user_email=user_email, 
            discipline_code=discipline_code
        )
        self.db.execute(stmt)
        self.db.commit()
        return True

    def remove(self, discipline_code: str):
        delete_statement = delete(models.Discipline).where(
            models.Discipline.discipline_code == discipline_code
        )
        self.db.execute(delete_statement)
        self.db.commit()
