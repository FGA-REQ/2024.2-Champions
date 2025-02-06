# models.py

from sqlalchemy import Column, String, ForeignKey, Table, Text, Integer, Date
from api.infra.sqlalchemy.config.db import Base
from sqlalchemy.orm import relationship

# Tabela associativa para o relacionamento muitos-para-muitos entre User e Discipline
user_discipline = Table(
    'user_discipline',
    Base.metadata,
    Column('user_email', String, ForeignKey('User.email'), primary_key=True),
    Column('discipline_code', String, ForeignKey('Discipline.discipline_code'), primary_key=True)
)

class Course(Base):
    __tablename__ = 'Course'
    
    course_name = Column(String, primary_key=True)
    degree_level = Column(String)

class User(Base):
    __tablename__ = 'User'
    
    email = Column(String, primary_key=True, index=True)
    password = Column(String)
    # Relacionamento muitos-para-muitos com Discipline
    disciplines = relationship('Discipline', secondary=user_discipline, back_populates='users')
    # Relacionamento 1:1 com Calendar
    tarefas = relationship('Tarefa', back_populates='user', cascade="all, delete")


class Discipline(Base):
    __tablename__ = 'Discipline'
    
    discipline_code = Column(String, primary_key=True, index=True)
    discipline_name = Column(String)
    # Relacionamento muitos-para-muitos com User
    users = relationship('User', secondary=user_discipline, back_populates='disciplines')

class Tarefa(Base):
    __tablename__ = 'Tarefa'
    
    tarefa_id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String, ForeignKey('User.email'))  # FK para User
    data = Column(Date)          # Data da tarefa
    assunto = Column(String)     # Assunto da tarefa

    
    # Relacionamento de volta para o usuário
    user = relationship('User', back_populates='tarefas')