from sqlalchemy.orm import Session
from api.infra.sqlalchemy.models import models
from api.schemas import schemas

class TarefaRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, tarefa: schemas.TarefaCreate, user_email: str):
        db_tarefa = models.Tarefa(
            user_email=user_email,
            data=tarefa.data,
            assunto=tarefa.assunto
        )
        self.db.add(db_tarefa)
        self.db.commit()
        self.db.refresh(db_tarefa)
        return db_tarefa

    def listar_por_usuario(self, user_email: str):
        return self.db.query(models.Tarefa).filter(
            models.Tarefa.user_email == user_email
        ).all()

    def deletar(self, tarefa_id: int):
        tarefa = self.db.query(models.Tarefa).get(tarefa_id)
        if tarefa:
            self.db.delete(tarefa)
            self.db.commit()
            return True
        return False
    
    def listar_por_data(self, data: str, user_email: str):
        return self.db.query(models.Tarefa).filter(
            models.Tarefa.data == data,
            models.Tarefa.user_email == user_email
        ).all()

    def atualizar(self, tarefa_id: int, tarefa: schemas.TarefaCreate, user_email: str):
        db_tarefa = self.db.query(models.Tarefa).filter(
            models.Tarefa.tarefa_id == tarefa_id,
            models.Tarefa.user_email == user_email
        ).first()
        
        if not db_tarefa:
            return None
        
        db_tarefa.assunto = tarefa.assunto
        db_tarefa.data = tarefa.data
        
        self.db.commit()
        self.db.refresh(db_tarefa)
        return db_tarefa