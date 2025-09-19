from fastapi import APIRouter, Form, Depends
from sqlmodel import Session

from db.session import get_session
from utils import generate_session_id
from services.vector_store import get_context
from services.llm import generate_answer
from config import HUGGINGFACE_API_KEY
from logging_utils import LogConfig, SessionLogger
from schemas.message_response import MessageResponse
from models.message import Message

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()
db = None


@router.post("/", response_model=MessageResponse)
async def ask_question(
    question: str = Form(...),
    session: Session = Depends(get_session)
) -> MessageResponse:
    session_id = generate_session_id()
    logger.log(session_id, f"Question received: {question}")

    context = get_context(db, question)

    answer = generate_answer(context, question, HUGGINGFACE_API_KEY)

    msg = Message(
        session_id=session_id,
        question=question,
        answer=answer
    )
    session.add(msg)
    session.commit()

    logger.log(session_id, f"Generated response: {answer}")
    return MessageResponse(message=answer)
