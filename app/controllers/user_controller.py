from services.user_service import UserService
from flask import jsonify, request

class UserController:

    def create_user():
        return jsonify(
            UserService.create_user(request_body=request.get_json())
        )
    
    def get_all_users():
        return jsonify(
            UserService.get_all_users()
        )
        
    def delete_user(user_id):
        return jsonify(
            UserService.delete_user(user_id=user_id)
        )