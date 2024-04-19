from fastapi import FastAPI
from routes import trivia

api = FastAPI(
    title="Trivia API",
    description="Api that provides trivia questions."
)

routers = [
    trivia.router
]

for router in routers:
    api.include_router(router=router)


