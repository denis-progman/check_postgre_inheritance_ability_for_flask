import logging
from flask import current_app

class APILog:
    def __init__(self, log_file="app.log"):
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(stream_handler)

    def log_debug(self, message):
        if current_app.config.get("DEBUG", False):
            self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, exception):
        self.logger.exception(exception)
