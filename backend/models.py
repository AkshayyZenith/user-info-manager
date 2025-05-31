from sqlalchemy import Column, Integer, String, Text
# from .database import Base
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    pincode = Column(String(10), nullable=False)
    address = Column(Text, nullable=False)