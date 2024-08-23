from flask import session

from services import UserService

class SessionService:
    
    def set_session(id):
        session["key"] = UserService.get_user_by_id(id)['user']['user_name']
        return session["key"]
    
    def get_session(id):
        if not session.get('key'):
           return "session is expired"
        return session.get('key')
    # __class__.set_session(id)