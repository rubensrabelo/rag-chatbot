from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class ModelName(str, Enum):
    GPT4_O = "gpt-4o"
    GPT4_O_MINI = "gpt-4o-mini"
    MISTRAL = "mistralai/Mistral-7B-Instruct-v0.2"
    TINYLLAMA = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GPT4_O_MINI)


class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName


class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime


class DeleteFileRequest(BaseModel):
    file_id: int
