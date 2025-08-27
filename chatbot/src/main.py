from fastapi import FastAPI, UploadFile, Form
from pdf_utils import extract_text_from_pdf
from vector_store import create_chroma_store, get_context
from llm import generate_answer

from config import HUGGINGFACE_API_KEY

app = FastAPI()
db = None


@app.get("/")
def home():
    return {"message": "Welcome to chatbot!"}


@app.post("/upload")
async def upload_pdf(file: UploadFile):
    global db
    content = extract_text_from_pdf(await file.read())
    db = create_chroma_store(content)
    return {"message": "PDF processado com sucesso"}


@app.post("/ask")
async def ask_question(question: str = Form(...)):
    context = get_context(db, question)
    answer = generate_answer(context, question, HUGGINGFACE_API_KEY)
    return {"answer": answer}
