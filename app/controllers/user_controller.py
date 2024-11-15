import json
import os
import pathlib
import hashlib
import httplib2

from services import UserService, AppService, GoogleAuthService, SessionService
from configs import Config
from flask import request, jsonify

class UserController:

    def get_users_by(field, field_value):
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(
            UserService.get_users_by(field=field, field_value=field_value, from_number=from_number, count=count)
        )
    
    def get_users():
        from_number = request.args.get('from', default=0, type=int)
        count = request.args.get('count', default=100, type=int)
        return jsonify(
            UserService.get_users_by(from_number=from_number, count=count)
        )
    
    def update_login():
        data = request.get_json()
        headers = dict(request.headers) 

        @AppService.is_token_valid(headers["X-Requested-With"])
        @AppService.check_min_str_length(data['google_sign_in_account']['login'], 3)  # 3 - min length of login to check
        def update_user_login():     
            google_sign_in_account_data = data.get('google_sign_in_account')
            google_id = GoogleAuthService.get_google_data(auth_code=google_sign_in_account_data['server_auth_code'])['google_id']
            response_body, status_code = UserService.update_login(google_id, google_sign_in_account_data['login'])
            return AppService.create_response(
                body = AppService.add_dict_value(response_body, 'session_token', SessionService.set_session(response_body['user']['id'])),
                status = status_code)

        return update_user_login()

    
    def get_user_by_id(user_id):
        return jsonify(
            UserService.get_user_by_id(user_id=user_id)
        )
    
    def create_user():
        return jsonify(
            UserService.create_user(request_body=request.get_json())
        )
    
    def update_user(user_id):
        return jsonify(
            UserService.update_user(user_id=user_id, request_body=request.get_json())
        )
    
    def delete_user(user_id):
        return jsonify(
            UserService.delete_user(user_id=user_id)
        )
    
    