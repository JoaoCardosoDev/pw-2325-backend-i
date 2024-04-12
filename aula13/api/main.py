from fastapi import FastAPI
from api.routes import products

api = FastAPI(
    title="Product API",
    description="Provides data for a catalog"
)

routers = [
    products.router
]

for router in routers:
    api.include_router(router=router)