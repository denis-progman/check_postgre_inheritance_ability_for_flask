from services import GoogleAuthService
from services import UserService
from services import AppService

from flask import request
from flask_api import status

class GoogleAuthController:
    def user_auth():
        # Get data from the app
        data = request.get_json()              
        auth_code = data.get('serverAuthCode')
        headers = dict(request.headers)  

        google_data_status = GoogleAuthService.get_google_data(auth_code=auth_code)

        return AppService.create_response(UserService.create_user(google_data_status), status.HTTP_200_OK, AppService.hash_code_to_send())