from dataclasses import dataclass


@dataclass
class LogFormatter:
    def format(self, session_id: str, message: str) -> str:
        return f"Session ID: {session_id}, Message: {message}"
