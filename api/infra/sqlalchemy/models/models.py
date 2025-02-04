from sqlalchemy import Column, Integer, String, ForeignKey
from api.infra.sqlalchemy.config.db import Base
from sqlalchemy.orm import relationship

class Course(Base):
  __tablename__ = 'Course'
  
  course_name = Column(String, primary_key=True)
  degree_level = Column(String)

class User(Base):
  __tablename__ = 'User'

  email = Column(String, primary_key=True, index=True)
  password = Column(String)
  disciplines = relationship('Discipline', back_populates='user')

class Discipline(Base):
  __tablename__ = 'Discipline'

  discipline_code = Column(String, primary_key=True, index=True)
  discipline_name = Column(String)
  user_email = Column(String, ForeignKey('User.email'))
  user = relationship('User', back_populates='disciplines')