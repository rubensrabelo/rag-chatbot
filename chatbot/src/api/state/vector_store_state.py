# Modificar esse padrão - Service Locator
store_cache: dict[str, object] = {}


def set_db(session_id: str, db) -> None:
    """
    Armazena um objeto de banco de dados no cache,
    vinculado ao session_id.
    """
    store_cache[session_id] = db


def get_db(session_id: str) -> object | None:
    """
    Recupera o objeto de banco de dados associado ao session_id.
    """
    return store_cache.get(session_id)
