from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from fastapi.middleware.cors import CORSMiddleware
from .routes import users, courses, disciplinas, cadastros
from api.infra.sqlalchemy.config.db import create_db
import os
#create_db()

templates = Jinja2Templates(directory='templates')

app = FastAPI()

origins = [
    'https://localhost:3000',
    "https://myapp.vercel.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# CSS PADRÃO
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), '../static')), name="static")

templates = Jinja2Templates(directory='templates')

@app.get('/')
async def root():
  return RedirectResponse(url='/login')

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(disciplinas.router)
app.include_router(cadastros.router)

# @app.get('/', response_class=HTMLResponse)
# async def root(request: Request):
#     return RedirectResponse('/login', status_code=status.HTTP_303_SEE_OTHER)

# @app.get('/login', response_class=HTMLResponse)
# async def login(request: Request):
#     return templates.TemplateResponse('login.html', { 'request': request })

# @app.get('/cadastro', response_class=HTMLResponse)
# async def cadastro(request: Request):
#     return templates.TemplateResponse('cadastro.html', { 'request': request})