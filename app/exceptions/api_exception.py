from core.api_log import APILog

class APIException(Exception):
    def __init__(self, status="error", http_code=400, message="An error occurred", details=None):
        self.status = status
        self.http_code = http_code
        self.message = message
        self.details = details or {}

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "details": self.details
        }

    def log(self):
        logger = APILog()
        logger.log_error(f"{self.status.upper()} ({self.http_code}): {self.message} | Details: {self.details}")
