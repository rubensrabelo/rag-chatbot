from fastapi import APIRouter, UploadFile

from utils import generate_session_id
from services.pdf_utils import extract_text_from_pdf
from services.vector_store import create_chroma_store
from logging_utils import LogConfig, SessionLogger
from schemas import MessageResponse

LogConfig().setup()
logger = SessionLogger()

router = APIRouter()
db = None


@router.post("/upload", response_model=MessageResponse)
async def upload_pdf(file: UploadFile) -> MessageResponse:
    global db
    session_id = generate_session_id()
    logger.log(session_id, f"Upload iniciado: {file.filename}")

    content = extract_text_from_pdf(await file.read())
    db = create_chroma_store(content)

    logger.log(session_id, "PDF processado com sucesso")
    return MessageResponse(message="PDF processed successfully")
