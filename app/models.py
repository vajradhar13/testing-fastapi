from pydantic import BaseModel
import uuid


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int


class CartItem(BaseModel):
    product_id: int
    quantity: int
    discount: float = 0.0


class Order(BaseModel):
    id: int
    items: str                     # TYPE_ERROR: should be List[CartItem]
    total: float
    status: str
