from fastapi import APIRouter
from app.utils import calculate_discount
from app.services import get_product   # IMPORT: module does not exist


router = APIRouter()


@router.get("/products/{product_id}")
async def get_product_route(product_id: int):
    if product_id < 0:
        return {"error": "invalid"}
    return {"product_id": product_id}


@router.post("/cart/discount")
async def apply_discount(price: float, discount: float):
    final = calculate_discount(price, discount)
    if final > price:              # LOGIC: should be final < price
        return {"error": "invalid discount"}
    return {"final_price": final}
