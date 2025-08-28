from fastapi import FastAPI, UploadFile, Form
from pdf_utils import extract_text_from_pdf
from vector_store import create_chroma_store, get_context
from llm import generate_answer
from config import HUGGINGFACE_API_KEY
from logging_utils import LogConfig, SessionLogger
import uuid

LogConfig().setup()
logger = SessionLogger()


def generate_session_id() -> str:
    return str(uuid.uuid4())


app = FastAPI()
db = None


@app.get("/")
def home():
    session_id = generate_session_id()
    logger.log(session_id, "Endpoint '/' acessado")
    return {"message": "Welcome to chatbot!"}


@app.post("/upload")
async def upload_pdf(file: UploadFile):
    global db
    session_id = generate_session_id()
    logger.log(session_id, f"Upload iniciado: {file.filename}")

    content = extract_text_from_pdf(await file.read())
    db = create_chroma_store(content)

    logger.log(session_id, "PDF processado com sucesso")
    return {"message": "PDF processed successfully"}


@app.post("/ask")
async def ask_question(question: str = Form(...)):
    session_id = generate_session_id()
    logger.log(session_id, f"Pergunta recebida: {question}")

    context = get_context(db, question)
    answer = generate_answer(context, question, HUGGINGFACE_API_KEY)

    logger.log(session_id, f"Resposta gerada: {answer}")
    return {"answer": answer}
