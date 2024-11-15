
from functools import wraps
import hashlib
from flask import make_response
from configs import Config

class AppService:
    token = Config.X_REQUESTED_WITH_TOKEN.encode()   
    hashed_token = str(hashlib.sha256(token).hexdigest())

    def hash_code(code):
        return str(hashlib.sha256(code.encode()).hexdigest())

    def create_response(body=None,
                        status=200, 
                        x_requested_with_value=None):
        response = make_response(body, status, x_requested_with_value)
        response.headers['X-Requested-With'] = __class__.hashed_token
        return response
    
    def add_dict_value(dict, key_name, value):
        dict[key_name] = value
        return dict
    
    @classmethod
    def check_min_str_length(__class__, str, n):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                if len(str) < n:
                    return "message: Login is too short! It must be at least 3 characters long.", 400
                return f(*args, **kwargs), 200
            return decorated_function
        return decorator
    
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