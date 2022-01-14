from operator import index
from sqlalchemy import Column, Integer, String

from .connection import Base

class Job(Base):
    __tablename__ = 'jobs'
    
    job_id = Column(Integer, primary_key=True, index=True)
    job_name = Column(String, unique=True, index=True)
    job_summary = Column(String)