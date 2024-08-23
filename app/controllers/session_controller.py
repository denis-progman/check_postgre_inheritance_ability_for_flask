from flask import session

from services import SessionService, UserService

class SessionController:

    def check_session(id):    
        return SessionService.get_session(id=id)