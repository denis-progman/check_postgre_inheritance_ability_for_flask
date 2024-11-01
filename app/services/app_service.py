
from functools import wraps
import hashlib
from flask import jsonify, make_response
from configs import Config

class AppService:
    token = Config.X_REQUESTED_WITH_TOKEN.encode()   
    hashed_token = str(hashlib.sha256(token).hexdigest())

    def create_response(body=None,
                        session_token=None,
                        status=200, 
                        x_requested_with_value=None):
        response = make_response(body, status, x_requested_with_value)
        response.headers['X-Requested-With'] = __class__.hashed_token
        response.headers['Session_Token'] = session_token
        return response
    
    # def is_valide(password_to_verify):
    #     if str(password_to_verify) == __class__.hashed_token:
    #         return True
    #     else:
    #         return False

    def hash_code(password):
        password_to_hash = password.encode()
        hashed_password = hashlib.sha256(password_to_hash).hexdigest()
        return hashed_password
    
    @classmethod
    def is_token_valid(__class__, password_to_verify):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                if str(password_to_verify) != __class__.hashed_token:
                    return "message: Token is not valid", 400
                else:
                    return f(*args, **kwargs)
            return decorated_function
        return decorator