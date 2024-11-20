import os
from datetime import timedelta
from services.session_service import SessionService
from flask import Flask, request
from core.exception_handler import ExceptionHandler
from core.middleware_manager import MiddlewareManager
from middleware.csrf_middleware import CSRFMiddleware
from middleware.validation_middleware import ValidationMiddleware
from router import router_rules
from db import db, migrate
from config import Config, current_config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(current_config)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)

# Configure session via SessionService
SessionService.configure_session(app)

# Register the global exception handler
@app.errorhandler(Exception)
def handle_exception(e):
    return ExceptionHandler.handle_exception(e)

# Initialize MiddlewareManager
middleware_manager = MiddlewareManager()

# Add ValidationMiddleware
validation_middleware = ValidationMiddleware(router_rules)
middleware_manager.add_middleware(validation_middleware)

# Add CSRFTokenCheck middleware
csrf_token_check = CSRFMiddleware()
middleware_manager.add_middleware(csrf_token_check)

# Middleware wrapper to create routes
def create_route(app, rule, methods, view_func, endpoint=None):
    def wrapped_view_func(*args, **kwargs):
        # Middleware execution logic
        response = middleware_manager.execute_middlewares(rule, request)
        if response:
            return response
        return view_func(*args, **kwargs)

    # Use a unique endpoint name if not provided
    endpoint = endpoint or view_func.__name__ + rule
    app.route(rule, methods=methods, endpoint=endpoint)(wrapped_view_func)

# Register all routes from router_rules
for route in router_rules:
    create_route(
        app,
        rule=route["rule"],
        methods=route["methods"],
        view_func=route["view_func"],
        endpoint=f"{route['rule']}_{'_'.join(route['methods'])}"  # Unique endpoint
    )

# Main entry point
if __name__ == "__main__":
    app.run()
