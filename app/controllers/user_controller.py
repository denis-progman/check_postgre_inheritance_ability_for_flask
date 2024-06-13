import os
import pathlib
import hashlib
import httplib2

from services import UserService
from flask import request, jsonify, session


from oauth2client import client
from googleapiclient import discovery


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
    
    def checking():
        # Get the string from the frontend
        data = request.get_json()
        input_string = data.get('code')
        auth_code = data.get('serverAuthCode')

        # Create a session
        session['input_string'] = input_string
        print(session['input_string'])

        # Create a special code (for example, a simple combination of string and some constant)
        special_code = input_string + 'SECRET_CODE'

        hashed_code = hashlib.sha256(special_code.encode()).hexdigest()

        # Send the hashed code back to the frontend
        response = {
            'hashed_code': hashed_code,
            'checking': 'successfully done'
        }

        # If this request does not have `X-Requested-With` header, this could be a CSRF

        # if not request.headers.get('X-Requested-With'):
        #     abort(403)

        # Set path to the Web application client_secret_*.json file you downloaded from the
        # Google API Console: https://console.cloud.google.com/apis/credentials
        CLIENT_SECRET_FILE = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

        # Exchange auth code for access token, refresh token, and ID token
        credentials = client.credentials_from_clientsecrets_and_code(
            CLIENT_SECRET_FILE,
            ['https://www.googleapis.com/auth/drive.appdata', 'profile', 'email'],
            auth_code)
        # Call Google API
        http_auth = credentials.authorize(httplib2.Http())
        drive_service = discovery.build('drive', 'v3', http=http_auth)
        appfolder = drive_service.files().get(fileId='appfolder').execute()

        # Get profile info from ID token
        userid = credentials.id_token['sub']
        email = credentials.id_token['email']
        
        response = {
            'hashed_code': hashed_code,
            'userid': userid,
            'email': email
        }
        # Hash the special code using SHA-256
        session['key'] = hashlib.sha256(special_code.encode()).hexdigest()
        return response