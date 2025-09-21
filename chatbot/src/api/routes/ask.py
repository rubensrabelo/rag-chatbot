from fastapi import APIRouter, Form, Depends
from sqlmodel import Session

from db.session import get_session
from utils import generate_session_id
from services.vector_store import get_context
from services.llm import generate_answer
from config import HUGGINGFACE_API_KEY
from logging_utils import LogConfig, SessionLogger
from schemas.message_response import MessageResponse
from services.history_service import save_history, get_history_context

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()
db = None


@router.post("/", response_model=MessageResponse)
async def ask_question(
    question: str = Form(...),
    session_id: str = Form(None),
    session: Session = Depends(get_session)
) -> MessageResponse:
    if not session_id:
        session_id = generate_session_id()

    logger.log(session_id, f"Question received: {question}")

    history_context = get_history_context(session, session_id)
    semantic_context = get_context(db, question)
    full_context = f"{history_context}\n\n{semantic_context}"

    answer = generate_answer(full_context, question, HUGGINGFACE_API_KEY)
    save_history(session, session_id, question, answer)

    logger.log(session_id, f"Generated response: {answer}")
    return MessageResponse(message=answer, session_id=session_id)
