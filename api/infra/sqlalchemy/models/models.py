from sqlalchemy import Column, Integer, String
from api.infra.sqlalchemy.config.db import Base

class Course(Base):
  __tablename__ = 'Course'
  
  course_name = Column(String, primary_key=True)
  degree_level = Column(String)
