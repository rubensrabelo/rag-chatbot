from fastapi import APIRouter

from utils import generate_session_id
from logging_utils import LogConfig, SessionLogger
from schemas import MessageResponse

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()


@router.get("/", response_model=MessageResponse)
def home() -> MessageResponse:
    session_id = generate_session_id()
    logger.log(session_id, "Endpoint '/' acessado")
    return MessageResponse(message="Welcome to chatbot!")
