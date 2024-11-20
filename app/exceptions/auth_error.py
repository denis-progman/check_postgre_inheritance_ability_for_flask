from exceptions.api_exception import APIException

class AuthenticationError(APIException):
    def __init__(self, message="Authentication failed. Please log in.", http_code=401, details=None):
        super().__init__(status="fail", http_code=http_code, message=message, details=details)
