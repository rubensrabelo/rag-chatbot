import sqlite3
from sqlmodel import SQLModel
from sqlalchemy import event, Engine

from .engine import engine


def create_db_and_tables() -> None:
    """
    Cria todas as tabelas definidas nos modelos
    SQLModel usando o engine configurado.
    """
    SQLModel.metadata.create_all(engine)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(
    dbapi_connection,
    connection_record
) -> None:
    """
    Ativa a verificação de integridade referencial
    no SQLite ao estabelecer conexão.
    """
    if type(dbapi_connection) is sqlite3.Connection:
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
