from fastapi import FastAPI
from app.api.v1 import items, users
from app.core.config import settings

app = FastAPI(
    title="FastAPI Template Project",
    description="Production-ready structure with versioned API and clean architecture",
    version=settings.API_VERSION
)

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["Items"])