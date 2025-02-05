from fastapi import APIRouter, Form, HTTPException, Request, status, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from api.infra.sqlalchemy.config.db import get_db
from api.infra.sqlalchemy.repositories.user import UserRepository
from api.infra.providers import hash_provider
from api.schemas.schemas import User

router = APIRouter(
    tags = ["Rotas de Autenticação de Usuário"] 
)

templates = Jinja2Templates(directory="templates")

# Update a user`s password 
@router.put('/')
def update_password(email:str, user: User, db: Session = Depends(get_db)):
  user_updated = UserRepository(db).update(email, user)
  return user_updated

# Delete route
@router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
  return UserRepository(db).remove(email)

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request, message: str = None):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get('/cadastro', response_class=HTMLResponse)
async def cadastro(request: Request):
    return templates.TemplateResponse('cadastro.html', {'request': request})

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.post("/login")
async def login_post(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = UserRepository(db).get_user_by_email(email)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ou senha incorretos!")

    if not hash_provider.verify_hash(password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senha incorreta!")

    return RedirectResponse("/dashboard", status_code=status.HTTP_303_SEE_OTHER)

@router.post('/cadastro')
async def cadastro_post(
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db)
):
    if password != confirm_password:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='As senhas nao coindicem!')

    user = UserRepository(db).get_user_by_email(email)
    if user:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado!")
    
    hashed_password = hash_provider.generate_hash(password)

    UserRepository(db).create_user(email, hashed_password)

    return RedirectResponse('/login?message=Cadastro+realizado+com+sucesso!', status_code=status.HTTP_303_SEE_OTHER)