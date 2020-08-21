"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Construct core Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import Flask routes
        from .interface import controller

        return app
