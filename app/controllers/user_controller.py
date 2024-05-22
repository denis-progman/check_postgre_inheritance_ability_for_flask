from services.user_service import UserService
from flask import jsonify, request, session
import hashlib
import os

class UserController:

    def create_user():
        return jsonify(
            UserService.create_user(request_body=request.get_json())
        )
    
    def update_user(user_id):
        return jsonify(
            UserService.update_user(user_id=user_id, request_body=request.get_json())
        )
    
    def get_all_users():
        return jsonify(
            UserService.get_all_users()
        )
<<<<<<< HEAD
=======
    
    def get_user_by_id(user_id):
        return jsonify(
            UserService.get_user_by_id(user_id=user_id)
        )
    
    def get_user_by_google_id(google_id):
        return jsonify(
            UserService.get_user_by_google_id(google_id=google_id)
        )
>>>>>>> bb8bfb8 (issue: checking bad request)
        
    def delete_user(user_id):
        return jsonify(
            UserService.delete_user(user_id=user_id)
<<<<<<< HEAD
        )
=======
        )
    
    def checking(str):
        # Get the string from the frontend
        data = request.json
        input_string = data.get('str')

        # Create a session
        session['input_string'] = input_string
        print(session['input_string'])

        # Create a special code (for example, a simple combination of string and some constant)
        special_code = input_string + 'SECRET_CODE'

        # Hash the special code using SHA-256
        hashed_code = hashlib.sha256(special_code.encode()).hexdigest()

        # Send the hashed code back to the frontend
        response = {
            'hashed_code': hashed_code,
            'checking': 'successfully done'
        }

        return jsonify(response)

>>>>>>> bb8bfb8 (issue: checking bad request)
