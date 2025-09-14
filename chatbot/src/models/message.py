from sqlmodel import SQLModel, Field


class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    session_id: str
    question: str
    answer: str
