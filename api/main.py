from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .routes import users, courses
from api.infra.sqlalchemy.config.db import create_db
import os
#create_db()

templates = Jinja2Templates(directory='templates')

app = FastAPI()

# CSS PADRÃO
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), '../static')), name="static")


app.include_router(users.router)
app.include_router(courses.router)

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return RedirectResponse('/login', status_code=status.HTTP_303_SEE_OTHER)

@app.get('/login', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse('login.html', { 'request': request })

@app.get('/cadastro', response_class=HTMLResponse)
async def cadastro(request: Request):
    return templates.TemplateResponse('cadastro.html', { 'request': request})