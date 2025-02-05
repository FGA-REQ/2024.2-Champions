from sqlalchemy.orm import Session
from sqlalchemy import delete
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

  def get(self):
    ...
  
  def remove(self, discipline_code:str):
    delete_statement = delete(models.Discipline).where(models.Discipline.discipline_code == discipline_code)
    
    self.db.execute(delete_statement)
    self.db.commit()
    #if disciplines:
     # self.bd.delete(disciplines)
      #self.db.commit()
      #return {"message": "Disciplina removida com sucesso"}
    #else: 
     # return{"error": "Disciplina não encontrada"}