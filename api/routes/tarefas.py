from datetime import date  # Importação necessária
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.infra.sqlalchemy.config.db import get_db
from api.infra.sqlalchemy.repositories.tarefa import TarefaRepository
from api.schemas.schemas import TarefaCreate, User  # Verifique se User está importado
from api.dependencies import get_current_user

router = APIRouter(
    prefix="/tarefas",
    tags=["Tarefas"]
)

@router.post("/", status_code=201)  # Alterado para incluir a barra final
def criar_tarefa(
    tarefa: TarefaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        if tarefa.data < date.today():
            raise HTTPException(
                status_code=400,
                detail="Não é possível adicionar tarefas em datas passadas"
            )
        
        db_tarefa = TarefaRepository(db).criar(tarefa, current_user.email)
        return db_tarefa

    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Formato de data inválido: {str(e)}"
        )

@router.get("/")
def listar_tarefas(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    repo = TarefaRepository(db)
    return repo.listar_por_usuario(current_user.email)

@router.delete("/{tarefa_id}")
def deletar_tarefa(
    tarefa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    repo = TarefaRepository(db)
    if not repo.deletar(tarefa_id):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"message": "Tarefa deletada com sucesso"}

@router.put("/{tarefa_id}")
def atualizar_tarefa(
    tarefa_id: int,
    tarefa: TarefaCreate,  # Usa o esquema correto
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    repo = TarefaRepository(db)
    tarefa_atualizada = repo.atualizar(tarefa_id, tarefa, current_user.email)

    if not tarefa_atualizada:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    return {"message": "Tarefa atualizada com sucesso", "tarefa": tarefa_atualizada}


