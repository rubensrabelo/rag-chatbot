from dataclasses import dataclass


@dataclass
class LogFormatter:
    """
    Utilitário para formatar mensagens de log com o identificador da sessão.
    """
    def format(self, session_id: str, message: str) -> str:
        return f"Session ID: {session_id}, Message: {message}"
