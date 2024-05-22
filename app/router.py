from flask import Flask
from controllers import auth_controller
from controllers.user_controller import UserController



route_rules = [
    # Main
    {"rule": "/", "methods": ["GET"], "view_func": lambda: "Hello world!"},
    {"rule": "/checking/<string:str>", "methods": ["POST"], "view_func": UserController.checking},

    # Google Authentication 
    {"rule": "/login", "methods": ["GET"], "view_func": auth_controller.login_window},
    {"rule": "/callback", "methods": ["GET"], "view_func": auth_controller.callback},
    {"rule": "/personal_account", "methods": ["GET"], "view_func": auth_controller.personal_account},
    {"rule": "/log_out", "methods": ["GET"], "view_func": auth_controller.account_exit},
    {"rule": "/google_auth", "methods": ["POST"], "view_func": auth_controller.user_auth},

    #Users
    {"rule": "/create_user", "methods": ["POST"], "view_func": UserController.create_user},
    {"rule": "/update_user/<int:user_id>", "methods": ["PUT"], "view_func": UserController.update_user},
    {"rule": "/get_all_users", "methods": ["GET"], "view_func": UserController.get_all_users},
<<<<<<< HEAD
=======
    {"rule": "/get_user_by_id/<int:user_id>", "methods": ["GET"], "view_func": UserController.get_user_by_id},
    {"rule": "/get_user_by_google_id/<int:google_id>", "methods": ["GET"], "view_func": UserController.get_user_by_google_id},
>>>>>>> bb8bfb8 (issue: checking bad request)
    {"rule": "/delete_user/<int:user_id>", "methods": ["DELETE"], "view_func": UserController.delete_user},
]

def routs_init(app: Flask):
    for route in route_rules:
        app.add_url_rule(**route)