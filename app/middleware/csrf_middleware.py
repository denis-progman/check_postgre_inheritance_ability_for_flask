from config import Config
from exceptions.auth_error import AuthenticationError
from exceptions.validation_error import ValidationError
import hashlib

class CSRFMiddleware:
    def __init__(self):
        pass

    def process_request(self, rule, request):
        """
        Validate the CSRF token for protected routes.
        """
        # Skip CSRF check for safe HTTP methods
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return None

        # Get the CSRF secret from the config
        secret_token =  str(hashlib.sha256(Config.CSRF_BACKEND_TOKEN.encode()).hexdigest())

        if not secret_token:
            raise SystemError(message="CSRF secret not configured in application settings.")

        # Extract the CSRF token from headers or request body
        token = request.headers.get("CSRF-Token") or request.json.get("csrf_token")

        if not token:
            raise ValidationError(
                message="Missing CSRF token. Please include the token in the header or body.",
                details={"method": request.method, "path": request.path}
            )

        if token != secret_token:
            raise AuthenticationError(
                message="Invalid CSRF token. Authentication failed.",
                details={"method": request.method, "path": request.path}
            )

        # Token is valid; continue the request
        return None
