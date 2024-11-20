from services.auth_service import AuthService
from services import UserService
from flask import request

class UserController:
    
    def get_users():
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return UserService.get_users_by(from_number=from_number, count=count)
    
    def register_user():
        data = request.get_json()
        return AuthService.register_user(**data)

    