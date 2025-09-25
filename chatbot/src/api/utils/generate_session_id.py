import uuid


def generate_session_id() -> str:
    """
    Gera um identificador único de sessão no formato UUID4.
    """
    return str(uuid.uuid4())
