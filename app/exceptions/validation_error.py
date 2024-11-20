from exceptions.api_exception import APIException

class ValidationError(APIException):
    def __init__(self, message="Invalid input. Please check your data and try again.", http_code=422, details=None):
        super().__init__(status="fail", http_code=http_code, message=message, details=details)
