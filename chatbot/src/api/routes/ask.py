from fastapi import APIRouter, Form

from utils import generate_session_id
from services.vector_store import get_context
from services.llm import generate_answer
from config import HUGGINGFACE_API_KEY
from logging_utils import LogConfig, SessionLogger
from schemas import MessageResponse

LogConfig().setup()
logger = SessionLogger()


router = APIRouter()
db = None


@router.post("/", response_model=MessageResponse)
async def ask_question(question: str = Form(...)) -> MessageResponse:
    session_id = generate_session_id()
    logger.log(session_id, f"Pergunta recebida: {question}")

    context = get_context(db, question)
    answer = generate_answer(context, question, HUGGINGFACE_API_KEY)

    logger.log(session_id, f"Resposta gerada: {answer}")
    return MessageResponse(message=answer)
