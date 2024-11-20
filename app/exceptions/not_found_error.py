from exceptions.api_exception import APIException

class NotFoundError(APIException):
    def __init__(self, message="The requested resource was not found.", http_code=404, details=None):
        super().__init__(status="fail", http_code=http_code, message=message, details=details)
