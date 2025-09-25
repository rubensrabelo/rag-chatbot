from sqlmodel import Session
from typing import Generator

from .engine import engine


def get_session() -> Generator[Session, None, None]:
    """
    Gerador de sessões de banco de dados usando o engine configurado.
    """
    with Session(engine) as session:
        yield session
