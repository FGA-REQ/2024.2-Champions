from fastapi import APIRouter, Form, HTTPException, Request, status, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from api.infra.sqlalchemy.config.db import get_db
from api.infra.sqlalchemy.repositories.user import UserRepository
from api.infra.sqlalchemy.repositories.discipline import DisciplineRepository
#from api.infra.sqlalchemy.repositories.media import MediaRepository
from api.infra.providers import hash_provider
from api.schemas.schemas import User
from api.dependencies import get_current_user

router = APIRouter(
    tags=["Rotas de Autenticação de Usuário"]
)

templates = Jinja2Templates(directory="templates")

# Atualizar senha do usuário
@router.put('/')
def update_password(email: str, user: User, db: Session = Depends(get_db)):
    user_updated = UserRepository(db).update(email, user)
    return user_updated

# Deletar usuário
@router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
    return UserRepository(db).remove(email)

# Página de login
@router.get("/login", response_class=HTMLResponse)
async def login(request: Request, message: str = None):
    return templates.TemplateResponse("login.html", {"request": request})

# Página de cadastro
@router.get('/cadastro', response_class=HTMLResponse)
async def cadastro(request: Request):
    return templates.TemplateResponse('cadastro.html', {'request': request})

# Página para alteração de senha
@router.get('/change-password', response_class=HTMLResponse)
async def change_password_page(request: Request):
    return templates.TemplateResponse('change-password.html', {'request': request})

# Dashboard
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("paginaUsuario.html", {"request": request})

# Página do calendário
@router.get("/calendar", response_class=HTMLResponse)
async def calendar_page(request: Request):
    return templates.TemplateResponse("calendar.html", {"request": request})

# Página para gerenciar disciplinas (buscar e adicionar)
@router.get('/discipline-management', response_class=HTMLResponse)
async def discipline_management_page(request: Request, search: str = None, db: Session = Depends(get_db)):
    if search:
        disciplinas = DisciplineRepository(db).search_discipline(search)
    else:
        disciplinas = DisciplineRepository(db).list_all()
    return templates.TemplateResponse("adicionar.html", {"request": request, "disciplinas": disciplinas, "search": search})

# Página para exibir as disciplinas associadas ao usuário
@router.get('/disciplines', response_class=HTMLResponse)
async def discipline_page(request: Request, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = UserRepository(db).get_user_by_email(current_user.email)
    disciplina = DisciplineRepository(db).search_discipline(request.query_params.get('code'))
    if disciplina:
        return templates.TemplateResponse("media.html", {"request": request, "disciplina": disciplina})
    return templates.TemplateResponse("cursos.html", {"request": request, "disciplinas": user.disciplines})


# Rota de login (processamento do formulário)
    
@router.post("/login")
async def login_post(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = UserRepository(db).get_user_by_email(email)
    if not user:
        return RedirectResponse(
            f'/login?message=Email ou senha incorretos!',
            status_code=status.HTTP_303_SEE_OTHER
        )
    if not hash_provider.verify_hash(password, user.password):
        return RedirectResponse(
            f'/login?message=Senha incorreta!',
            status_code=status.HTTP_303_SEE_OTHER
        )
    # Cria uma resposta de redirecionamento e define o cookie com o e-mail do usuário
    response = RedirectResponse("/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="user_email", value=email)
    return response
    

# Rota de cadastro (processamento do formulário)
@router.post('/cadastro')
async def cadastro_post(
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db)
):
    if password != confirm_password:
        return RedirectResponse(f'/cadastro?message=As senhas não coindicem!', status_code=status.HTTP_303_SEE_OTHER)
    user = UserRepository(db).get_user_by_email(email)
    if user:
        return RedirectResponse(f'/cadastro?message=Email já cadastrado!', status_code=status.HTTP_303_SEE_OTHER)
    
    hashed_password = hash_provider.generate_hash(password)
    UserRepository(db).create_user(email, hashed_password)
    return RedirectResponse('/login?message=Cadastro+realizado+com+sucesso!', status_code=status.HTTP_303_SEE_OTHER)

# Rota de alteração de senha (processamento do formulário)
@router.post('/change-password')
async def change_password(
    email: str = Form(...),
    new_password: str = Form(...),
    confirm_new_password: str = Form(...),
    db: Session = Depends(get_db)
):
    if new_password != confirm_new_password:
        return RedirectResponse(f'/change-password?message=As senhas não coincidem!', status_code=status.HTTP_303_SEE_OTHER)
    
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_email(email)
    if not user:
        return RedirectResponse(f'/change-password?message=Usuário não encontrado!', status_code=status.HTTP_303_SEE_OTHER)
    
    hashed_new_password = hash_provider.generate_hash(new_password)
    user_updated = user_repo.update_password(email, hashed_new_password)
    if not user_updated:
        raise HTTPException(status_code=500, detail='Erro ao atualizar a senha!')
    
    return RedirectResponse('/login?message=Senha atualizada com sucesso!', status_code=303)

# Rota para associar disciplina ao usuário (processamento do formulário)
@router.post('/discipline-management')
async def discipline_add(
    discipline_code: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    repo = DisciplineRepository(db)
    success = repo.add_user_to_discipline(current_user.email, discipline_code)
    if not success:
        # Se já existe a associação, redireciona com mensagem adequada
        return RedirectResponse(
            f'/discipline-management?message=Você já está cadastrado nesta disciplina!',
            status_code=status.HTTP_303_SEE_OTHER
        )
    return RedirectResponse(
        f'/discipline-management?message=Disciplina adicionada com sucesso!',
        status_code=status.HTTP_303_SEE_OTHER
    )


@router.post('/disciplines')
async def discipline_calc(
    code: str = Form(...),
    turma:  str = Form(...),
    media:  str = Form(...),
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    media = media.replace('+', '?')
    print(media)
    return RedirectResponse(
        f'/disciplines?code={code}&turma={turma}&calc={media}',
        status_code=status.HTTP_303_SEE_OTHER
    )

