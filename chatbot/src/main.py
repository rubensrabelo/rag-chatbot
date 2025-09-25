from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from db import create_db_and_tables
from api.api_controller import api_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Executa tarefas de inicialização da aplicação,
    como a criação das tabelas do banco de dados.
    """
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)
