from exceptions.api_exception import APIException


class UserError(APIException):
    def __init__(self, message="Something went wrong. Please follow the instructions provided.", http_code=400, details=None):
        super().__init__(status="fail", http_code=http_code, message=message, details=details)
