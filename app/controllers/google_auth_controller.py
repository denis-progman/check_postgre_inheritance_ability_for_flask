from services import GoogleAuthService
from services import UserService
from services import AppService
from services import SessionService
from configs import Config

from flask import request
from flask_api import status

class GoogleAuthController:
    def user_auth():
        # Get data from the app
        data = request.get_json()              
        auth_code = data.get('serverAuthCode')
        headers = dict(request.headers)
        print(AppService.is_valide(headers["X-Requested-With"]))
        print(data.get('id'))

        google_data_status = GoogleAuthService.get_google_data(auth_code=auth_code)

        # user_object = UserService.is_user_exist(google_data_status)

        return AppService.create_response(
            UserService.is_user_exist(google_data_status),
            status.HTTP_200_OK,
            AppService.hash_code(Config.PASSWORD_TO_HASH),
            SessionService.set_session(UserService.get_users_by('google_id', google_data_status['google_id'])['user']['id']))
        
        # UserService.get_user_by_login(UserService.get_users_by('google_id', google_data_status['google_id'])['user']['login'])