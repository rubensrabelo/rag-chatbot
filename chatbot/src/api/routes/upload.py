from fastapi import APIRouter, UploadFile, Form

from api.utils import generate_session_id
from api.services.pdf_utils import extract_text_from_pdf
from api.services.vector_store import create_chroma_store
from api.state.vector_store_state import set_db
from logging_utils import LogConfig, SessionLogger
from schemas import MessageResponse

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()


@router.post("/upload", response_model=MessageResponse)
async def upload_pdf(
    file: UploadFile,
    session_id: str = Form(None)
) -> MessageResponse:
    if not session_id:
        session_id = generate_session_id()

    logger.log(session_id, f"Upload iniciado: {file.filename}")

    content = extract_text_from_pdf(await file.read())
    db = create_chroma_store(content)

    set_db(session_id, db)

    logger.log(session_id, "PDF processed successfully")
    return MessageResponse(
        message="PDF processed successfully",
        session_id=session_id
    )
