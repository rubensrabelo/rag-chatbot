from fastapi import APIRouter

from logging_utils import LogConfig, SessionLogger
from schemas import MessageResponse

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()


@router.get("/", response_model=MessageResponse)
def home() -> MessageResponse:
    logger.log("Endpoint '/' acessado")
    return MessageResponse(message="Welcome to chatbot!")
