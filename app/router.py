from flask import Flask
from controllers import UserController
from controllers import GoogleAuthController
from controllers import AppController
from controllers import SessionController

route_rules = [
    # Main
    {"rule": "/", "methods": ["GET"], "view_func": lambda: "Hello worldddddd!"},

    # Google Auth
    {"rule": "/user_auth", "methods": ["POST"], "view_func": GoogleAuthController.google_auth_controller},
    {"rule": "/register_user", "methods": ["POST"], "view_func": UserController.update_login},

    # User api
    {"rule": "/get_users", "methods": ["GET"], "view_func": UserController.get_users},
    {"rule": "/get_users_by/<field>/<field_value>", "methods": ["GET"], "view_func": UserController.get_users_by},
    {"rule": "/get_user_by_id/<int:user_id>", "methods": ["GET"], "view_func": UserController.get_user_by_id},
    {"rule": "/create_user", "methods": ["POST"], "view_func": UserController.create_user},
    {"rule": "/update_user/<int:user_id>", "methods": ["PUT"], "view_func": UserController.update_user},
    {"rule": "/delete_user/<int:user_id>", "methods": ["DELETE"], "view_func": UserController.delete_user},

    # Tests
    {"rule": "/session_test/<int:id>", "methods": ["GET"], "view_func": SessionController.get_session},
]

def routs_init(app: Flask):
    for route in route_rules:
        app.add_url_rule(**route)