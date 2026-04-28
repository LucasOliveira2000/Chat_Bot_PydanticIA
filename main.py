from fastapi import FastAPI, APIRouter
from app.middlewares.cors_middleware import CorsMiddleware
from app.routers import routers

app = FastAPI()

app.middleware("http")(
    CorsMiddleware()
)
for router in routers:
    app.include_router(router)