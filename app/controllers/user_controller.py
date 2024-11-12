import json
import os
import pathlib
import hashlib
import httplib2

from services import UserService, AppService, GoogleAuthService
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
        # Get data from the app
        data = request.get_json()
        headers = dict(request.headers) 
        @AppService.is_token_valid(headers["X-Requested-With"])
        def update_user_login():     
            if Config.GOOGLE_SIGN_IN_ACCOUNT in data.keys():
                user_data = data.get('google_sign_in_account')
                print(f"second request: {user_data}")
                google_id = GoogleAuthService.get_google_data(auth_code=user_data['server_auth_code'])['google_id']
                print(google_id)
                return AppService.create_response(
                    jsonify(UserService.update_login(google_id, user_data['login'])))
            elif 'apple_id' in data.keys():
                pass

            elif 'facebook_id' in data.keys():
                pass
            else:
                return 'Unknown service'

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
    
    