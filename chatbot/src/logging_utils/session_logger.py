from dataclasses import dataclass, field
import logging
from logging_utils.formatter import LogFormatter


@dataclass
class SessionLogger:
    """
    Classe responsável por registrar mensagens de log associadas a uma sessão.
    """

    formatter: LogFormatter = field(default_factory=LogFormatter)
    logger: logging.Logger = field(default_factory=logging.getLogger)

    def log(self, session_id: str, message: str, level: str = "info") -> None:
        """
        Registra uma mensagem de log com o nível especificado.
        """
        formatted = self.formatter.format(session_id, message)
        if level == "info":
            self.logger.info(formatted)
        elif level == "error":
            self.logger.error(formatted)
        elif level == "warning":
            self.logger.warning(formatted)
        else:
            self.logger.debug(formatted)
