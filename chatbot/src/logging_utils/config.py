from dataclasses import dataclass
import logging
import os


# Quebrar essa classe em outras diferentes
@dataclass
class LogConfig:
    """
    Configuração de logging para a aplicação.
    """

    log_dir: str = "logs"
    log_name: str = "app.log"
    level: int = logging.INFO

    def setup(self):
        """
        Inicializa o sistema de logging.

        - Cria o diretório de logs, se necessário.
        - Configura o logger raiz com handlers para arquivo e console.
        - Aplica formatação padrão com timestamp, nível e mensagem.
        """
        os.makedirs(self.log_dir, exist_ok=True)
        log_path = os.path.join(self.log_dir, self.log_name)

        root_logger = logging.getLogger()
        if root_logger.hasHandlers():
            root_logger.handlers.clear()

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setLevel(self.level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        root_logger.setLevel(self.level)
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)
