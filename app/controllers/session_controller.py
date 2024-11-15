from flask import session

from services import SessionService, UserService

class SessionController:

    def set_session(id):    
        return SessionService.set_session(id=id)

    def get_session(id):    
        return SessionService.is_session_expired(id=id)