from controllers.main_controller import MainController
from services.auth_service import AuthService
from services.user_service import UserService
from flask import request

class AuthController(MainController):
    def auth_controller():
        request_data = request.get_json()
        return AuthService.auth_user(
            service_auth_id_field_name=request_data["service_auth_id_field_name"], 
            service_auth_code=request_data["service_auth_code"])
    