import hashlib
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

        if AppService.is_valid(headers["X-Requested-With"]):
            google_data_status = GoogleAuthService.get_google_data(auth_code=auth_code)
            return AppService.create_response(
                UserService.is_user_exist(google_data_status),
                SessionService.set_session(UserService.get_users_by('google_id', google_data_status['google_id'])['user']['id']))
        else:
            return 'Hashed Token is not valid'
            

        # google_data_status = GoogleAuthService.get_google_data(auth_code=auth_code)

        # user_object = UserService.is_user_exist(google_data_status)
        
        # return AppService.create_response(
        #         UserService.is_user_exist(google_data_status),
                # SessionService.set_session(UserService.get_users_by('google_id', google_data_status['google_id'])['user']['id']))
    
    # def google_data_response(auth_code):
    #     google_data_status = GoogleAuthService.get_google_data(auth_code=auth_code)

        # user_object = UserService.is_user_exist(google_data_status)
        
        # return AppService.create_response(
        #         UserService.is_user_exist(google_data_status),
        #         SessionService.set_session(UserService.get_users_by('google_id', google_data_status['google_id'])['user']['id']))