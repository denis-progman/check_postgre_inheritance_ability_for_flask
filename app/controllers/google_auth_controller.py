from services import AppService, UserService, GoogleAuthService
from configs import Config

from flask import request

class GoogleAuthController:
    def google_auth_controller():
        auth_data = request.get_json()
        auth_headers = dict(request.headers)
        
        @AppService.is_token_valid(auth_headers["X-Requested-With"])
        def google_auth_controller():
            google_sign_in_account_data = auth_data.get('google_sign_in_account')
            user_google_data = GoogleAuthService.get_google_data(auth_code=google_sign_in_account_data['server_auth_code'])
            response_body, status_code = UserService.is_user_exist(user_google_data)
            
            return AppService.create_response(
                        body = response_body,
                        status=status_code)
        return google_auth_controller()