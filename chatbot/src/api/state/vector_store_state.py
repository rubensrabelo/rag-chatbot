store_cache: dict[str, object] = {}


def set_db(session_id: str, db):
    store_cache[session_id] = db


def get_db(session_id: str):
    return store_cache.get(session_id)
