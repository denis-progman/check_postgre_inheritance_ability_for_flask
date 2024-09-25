import hashlib
import os
from flask import make_response
from configs import Config

class AppService:
    password = Config.PASSWORD_TO_HASH

    def create_response(body=None, status=200, header_value=None, session_status=None):
        response = make_response(body, 200)
        response.headers['X-Requested-With'] = header_value
        response.headers['Session_Status'] = session_status
        return response
    
    def is_valide(password_to_verify):
        if str(password_to_verify) == str(hashlib.sha256(__class__.password).hexdigest()):
            return 'Password is correct'
        else:
            return 'Invalid password'


    def hash_code_to_send():
        hashed_password = hashlib.sha256(__class__.password).hexdigest()
        return hashed_password