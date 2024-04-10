from fastapi import FastAPI
from catalog.routes import(
    products
)

app = FastAPI(
    title="Product API",
    description="This API provides data for out catalog",
)

routers = [
    products.router
]

for router in routers:
    app.include_router(router=router)

@app.get("/product")
def 
