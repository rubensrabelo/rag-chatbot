from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class History(SQLModel, table=True):
    """
    Modelo de tabela que registra o histórico de interações em uma sessão.
    """
    id: int | None = Field(default=None, primary_key=True)
    session_id: str
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    question: str
    answer: str
