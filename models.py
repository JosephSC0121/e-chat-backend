# myapp/models.py
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    size = Column(String(50), nullable=False)
    units = Column(Integer, nullable=False)
    discount = Column(Boolean, nullable=False)
