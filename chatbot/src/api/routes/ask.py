from fastapi import APIRouter, HTTPException, Form, Depends
from sqlmodel import Session

from db.session import get_session
from api.services.vector_store import get_context
from api.services.llm import generate_answer
from api.state.vector_store_state import get_db
from api.services.history_service import save_history, get_history_context
from config import HUGGINGFACE_API_KEY
from logging_utils import LogConfig, SessionLogger
from schemas.message_response import MessageResponse

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()


@router.post("/", response_model=MessageResponse)
async def ask_question(
    question: str = Form(...),
    session_id: str = Form(...),
    session: Session = Depends(get_session)
) -> MessageResponse:
    logger.log(session_id, f"Question received: {question}")

    db = get_db(session_id)
    if not db:
        raise HTTPException(
            status_code=400,
            detail="No PDFs were uploaded for this session."
        )

    history_context = get_history_context(session, session_id)
    semantic_context = get_context(db, question)
    full_context = f"{history_context}\n\n{semantic_context}"

    answer = generate_answer(full_context, question, HUGGINGFACE_API_KEY)
    save_history(session, session_id, question, answer)

    logger.log(session_id, f"Generated response: {answer}")
    return MessageResponse(message=answer, session_id=session_id)
