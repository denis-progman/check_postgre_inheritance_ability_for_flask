import os
from config import Config
from flask import session
import datetime
import hashlib
from exceptions.auth_error import AuthenticationError

class SessionService():
    @staticmethod
    def configure_session(app):
        """Configure session settings for the Flask app."""
        app.config["SESSION_TYPE"] = Config.SESSION_TYPE
        app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
        app.permanent_session_lifetime = datetime.timedelta(minutes=Config.SESSION_LIFE_TIME)

    @staticmethod
    def get_session_token(code):
        return str(hashlib.sha256(code.encode()).hexdigest())
    
    @staticmethod
    def set_session(user_id):
        session["key"] = __class__.get_session_token(str(user_id) + ' ' + str(datetime.datetime.now()))
        return session["key"]
    
    @staticmethod
    def is_session_expired(user_id):
        try:
            if not session.get(user_id):
                raise AuthenticationError("Session is expired")
            return session.get('key')
        except KeyError as e:
            return str(e)
