from api.clients import get_product_by_id, get_products
from api.models import Product
from typing import List
from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix="/products", tags=["Products"])

@router.get("")
def get_all_products()->List[Product]:
    result = [
        Product(**product)
        for product in get_products(db="/app/db.json")
    ]
    return result

@router.get("/{product_id:str}")
def get_product(product_id:str)->Product:
    
    
    result:Product | None = get_product_by_id(product_id=product_id)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    assert type(result) is Product

    return result
