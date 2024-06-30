from sqlalchemy import Column, Integer, String, Boolean
from models.database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    size = Column(String(50), nullable=False)
    units = Column(Integer, nullable=False)
    discount = Column(Boolean, nullable=False)
