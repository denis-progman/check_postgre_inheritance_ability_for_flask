import datetime

from flask import session
from services import UserService
from services import AppService

class SessionService:
    
    def set_session(id):
        session["key"] = AppService.hash_code(str(UserService.get_user_by_id(id)['user']['id']) + ' ' + str(datetime.datetime.now()))
        return session["key"]
    
    def is_session_expired(id):
        try:
            if not session.get('key'):
                raise KeyError("Session is expired")
            return session.get('key')
        except KeyError as e:
            return str(e)
        