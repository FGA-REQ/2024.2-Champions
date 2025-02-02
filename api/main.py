from fastapi import FastAPI
from .routes import users, courses
from api.infra.sqlalchemy.config.db import create_db

create_db()

app = FastAPI()

app.include_router(users.router)
app.include_router(courses.router)