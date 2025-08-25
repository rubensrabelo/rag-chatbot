from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
import logging


@dataclass
class StructuredLog:
    event_type: str
    session_id: str
    model: str
    user_query: str = None
    ai_response: str = None
    timestamp: str = datetime.now(timezone.utc)

    def log(self, logger_name="app_logger"):
        logger = logging.getLogger(logger_name)
        logger.info(json.dumps(asdict(self)))