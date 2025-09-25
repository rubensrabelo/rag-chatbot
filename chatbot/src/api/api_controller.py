from fastapi import APIRouter

from .routes import (
    ask_router,
    upload_router,
    home_router
)

api_router = APIRouter()

api_router.include_router(home_router, prefix="/home", tags=["Home"])
api_router.include_router(ask_router, prefix="/questions", tags=["Question"])
api_router.include_router(upload_router, prefix="/Uploads", tags=["Upload"])
