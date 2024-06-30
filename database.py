import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Boolean
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from pydantic import BaseModel

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')

# Configuración de la conexión a la base de datos
URL_DATABASE = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia de la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Depends(get_db)

Base = declarative_base()

# Modelo de la base de datos
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    size = Column(String(50), nullable=False)
    units = Column(Integer, nullable=False)
    discount = Column(Boolean, nullable=False)

# Modelo Pydantic
class ProductBase(BaseModel):
    name: str
    price: float
    size: str
    units: int
    discount: bool

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True

# Inicialización de FastAPI
app = FastAPI()

# Ruta para obtener todos los productos
@app.get('/products/', response_model=List[ProductOut])
def read_products(skip: int = 0, limit: int = 10, db: Session = db_dependency):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

# Ruta para crear un nuevo producto
@app.post('/products/', response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = db_dependency):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Ruta para obtener un producto por ID
@app.get('/products/{product_id}', response_model=ProductOut)
def read_product(product_id: int, db: Session = db_dependency):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Ruta para actualizar un producto
@app.put('/products/{product_id}', response_model=ProductOut)
def update_product(product_id: int, product: ProductCreate, db: Session = db_dependency):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

# Ruta para eliminar un producto
@app.delete('/products/{product_id}')
def delete_product(product_id: int, db: Session = db_dependency):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted"}
