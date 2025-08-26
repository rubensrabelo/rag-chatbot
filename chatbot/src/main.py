from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chain import process
import uvicorn

app = FastAPI(title="Chatbot API", 
              description="API para chatbot com UAE-Large-V1 e FLAN-T5-Large",
              version="1.0.0")


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    embedding: list
    embedding_full_size: int


@app.get("/")
def home():
    return {"message": "Welcome to the chatbot API!", "status": "active"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        result = process(req.question)
        return result
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno no processamento da pergunta")


@app.get("/health")
def health_check():
    return {"status": "healthy", "model_embedding": "WhereIsAI/UAE-Large-V1", "model_llm": "google/flan-t5-large"}
