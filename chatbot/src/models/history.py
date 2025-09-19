from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class History(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    session_id: str
    timestamp: datetime = Field(default_factory=timezone.utc)
    question: str
    answer: str
