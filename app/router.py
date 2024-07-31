from flask import Flask, send_from_directory
from controllers import UserController
from controllers import GoogleAuthController
from controllers import AppController

route_rules = [
    # Main
    {"rule": "/", "methods": ["GET"], "view_func": lambda: "Hello worldddddd!"},

    # Test
    {"rule": "/test/<string:password_to_verify>", "methods": ["POST"], "view_func": AppController.password_verify},
    {"rule": "/test2", "methods": ["GET"], "view_func": AppController.get_hashed_password},

    {"rule": "/user_auth", "methods": ["POST"], "view_func": GoogleAuthController.user_auth},

    # User api
    {"rule": "/get_users", "methods": ["GET"], "view_func": UserController.get_users},
    {"rule": "/get_users_by/<field>/<field_value>", "methods": ["GET"], "view_func": UserController.get_users_by},
    {"rule": "/get_user_by_id/<int:user_id>", "methods": ["GET"], "view_func": UserController.get_user_by_id},
    {"rule": "/create_user", "methods": ["POST"], "view_func": UserController.create_user},
    {"rule": "/update_user/<int:user_id>", "methods": ["PUT"], "view_func": UserController.update_user},
    {"rule": "/delete_user/<int:user_id>", "methods": ["DELETE"], "view_func": UserController.delete_user},
]

def routs_init(app: Flask):
    for route in route_rules:
        app.add_url_rule(**route)
