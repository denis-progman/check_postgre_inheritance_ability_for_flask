from flask import Flask, send_from_directory
from controllers import UserController
from controllers import GamerController
from controllers import ViewerController
from controllers import LoserController
from controllers import google_auth_controller

route_rules = [
    # Main
    {"rule": "/", "methods": ["GET"], "view_func": lambda: "Hello worldddddd!"},

    {"rule": "/checking", "methods": ["POST"], "view_func": google_auth_controller.checking},
    # {"rule": "/callback", "methods": ["GET"], "view_func": google_auth_controller.callback},

    # User api
    {"rule": "/get_users", "methods": ["GET"], "view_func": UserController.get_users},
    {"rule": "/get_users_by/<field>/<field_value>", "methods": ["GET"], "view_func": UserController.get_users_by},
    {"rule": "/get_user_by_id/<int:user_id>", "methods": ["GET"], "view_func": UserController.get_user_by_id},
    {"rule": "/create_user", "methods": ["POST"], "view_func": UserController.create_user},
    {"rule": "/update_user/<int:user_id>", "methods": ["PUT"], "view_func": UserController.update_user},
    {"rule": "/delete_user/<int:user_id>", "methods": ["DELETE"], "view_func": UserController.delete_user},

    # Gamer api
    {"rule": "/get_gamers", "methods": ["GET"], "view_func": GamerController.get_gamers},
    {"rule": "/get_gamers_by/<field>/<field_value>", "methods": ["GET"], "view_func": GamerController.get_gamers_by},
    {"rule": "/get_gamer_by_id/<int:id>", "methods": ["GET"], "view_func": GamerController.get_gamer_by_id},
    {"rule": "/create_gamer", "methods": ["POST"], "view_func": GamerController.create_gamer},
    {"rule": "/update_gamer/<int:id>", "methods": ["PUT"], "view_func": GamerController.update_gamer},
    {"rule": "/delete_gamer/<int:id>", "methods": ["DELETE"], "view_func": GamerController.delete_gamer},

    # Viewer api
    {"rule": "/get_viewers", "methods": ["GET"], "view_func": ViewerController.get_viewers},
    {"rule": "/get_viewers_by/<field>/<field_value>", "methods": ["GET"], "view_func": ViewerController.get_viewers_by},
    {"rule": "/get_viewer_by_id/<int:id>", "methods": ["GET"], "view_func": ViewerController.get_viewer_by_id},
    {"rule": "/create_viewer", "methods": ["POST"], "view_func": ViewerController.create_viewer},
    {"rule": "/update_viewer/<int:id>", "methods": ["PUT"], "view_func": ViewerController.update_viewer},
    {"rule": "/delete_viewer/<int:id>", "methods": ["DELETE"], "view_func": ViewerController.delete_viewer},

    # Loser api
    {"rule": "/get_losers", "methods": ["GET"], "view_func": LoserController.get_losers},
    {"rule": "/get_losers_by/<field>/<field_value>", "methods": ["GET"], "view_func": LoserController.get_losers_by},
    {"rule": "/get_loser_by_id/<int:id>", "methods": ["GET"], "view_func": LoserController.get_loser_by_id},
    {"rule": "/create_loser", "methods": ["POST"], "view_func": LoserController.create_loser},
    {"rule": "/update_loser/<int:id>", "methods": ["PUT"], "view_func": LoserController.update_loser},
    {"rule": "/delete_loser/<int:id>", "methods": ["DELETE"], "view_func": LoserController.delete_loser},
]

def routs_init(app: Flask):
    for route in route_rules:
        app.add_url_rule(**route)
