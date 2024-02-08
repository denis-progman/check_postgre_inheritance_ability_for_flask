from flask import Flask, send_from_directory
from controllers import UserController
from controllers import GamerController

route_rules = [
    # Main
    {"rule": "/", "methods": ["GET"], "view_func": lambda: "Hello world!"},
    # User api
    {"rule": "/get_users", "methods": ["GET"], "view_func": UserController.get_users},
    {"rule": "/create_user", "methods": ["POST"], "view_func": UserController.create_user},
    {"rule": "/delete_user/<int:user_id>", "methods": ["DELETE"], "view_func": UserController.delete_user},

    # Gamer api
    {"rule": "/get_gamers", "methods": ["GET"], "view_func": GamerController.get_all},
    {"rule": "/get_gamer/<field>/<field_value>", "methods": ["GET"], "view_func": GamerController.get_by},
    {"rule": "/get_gamer/<int:id>", "methods": ["GET"], "view_func": GamerController.get_by_id},
    {"rule": "/create_gamer", "methods": ["POST"], "view_func": GamerController.create},
    {"rule": "/update_gamer/<int:id>", "methods": ["PUT"], "view_func": GamerController.update},
    {"rule": "/delete_gamer/<int:id>", "methods": ["DELETE"], "view_func": GamerController.delete},
]

def routs_init(app: Flask):
    for route in route_rules:
        app.add_url_rule(**route)
