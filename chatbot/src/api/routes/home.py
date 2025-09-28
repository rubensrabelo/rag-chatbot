from fastapi import APIRouter

from api.utils import generate_session_id
from logging_utils import LogConfig, SessionLogger
from schemas import MessageResponse

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()


@router.get("/", response_model=MessageResponse)
def home() -> MessageResponse:
    """
    Endpoint raiz da API.
    Gera um session_id, registra o acesso via logger
    e retorna uma mensagem de boas-vindas.
    """
    session_id = generate_session_id()
    logger.log(session_id, "Endpoint '/' acessado")
    return MessageResponse(message="Welcome to chatbot!")
