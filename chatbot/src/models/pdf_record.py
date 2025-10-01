from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class PDFRecord(SQLModel, table=True):
    """
    Modelo SQLModel que representa um registro de upload de arquivo PDF.
    """
    id: int | None = Field(default=None, primary_key=True)
    filename: str
    session_id: str
    upload_time: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    description: str | None = None
