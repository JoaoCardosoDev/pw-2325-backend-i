from pydantic import BaseModel

class Product():
    name: str
    sku: int
    price: float
    enabled: bool
    id: int