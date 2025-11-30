from fastapi import APIRouter

from app.api.routes import assets

api_router = APIRouter()

api_router.include_router(assets.router)
