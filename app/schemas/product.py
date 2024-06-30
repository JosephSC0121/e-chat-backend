from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    type: str
    price: float
    size: str
    units: int
    discount: bool
