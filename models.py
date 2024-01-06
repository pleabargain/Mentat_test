from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    favorite_pet = Column(String)