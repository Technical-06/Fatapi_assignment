from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'todo'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(20))
    nombre = Column(String(200))
    rol = Column(String(20))
    estado = Column(Integer)

