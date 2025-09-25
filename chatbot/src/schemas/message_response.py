from pydantic import BaseModel


class MessageResponse(BaseModel):
    """
    Modelo de resposta padrão contendo uma única mensagem de texto.
    """
    message: str
