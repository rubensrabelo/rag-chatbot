from .home import router as home_router
from .ask import router as ask_router
from .upload import router as upload_router

__all__ = [
    "home_router",
    "ask_router",
    "upload_router",
]
