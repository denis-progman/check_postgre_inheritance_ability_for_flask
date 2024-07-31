import hashlib
import os
from flask import make_response

class AppService:
    password = os.getenv('PASSWORD_TO_HASH').encode()
    salt = os.getenv('SALT').encode()

    def create_response(body=None, status=200, header_value=None):
        response = make_response(body, 200)
        response.headers['X-Requested-With'] = header_value
        return response
    
    def is_valide(password_to_verify):
        if str(password_to_verify) == str(hashlib.pbkdf2_hmac('sha256', __class__.password, __class__.salt, 100000)):
            return 'Password is correct'
        else:
            return 'Invalid password'


    def hash_code_to_send():
        hashed_password = hashlib.pbkdf2_hmac('sha256', __class__.password, __class__.salt, 100000)
        return hashed_password