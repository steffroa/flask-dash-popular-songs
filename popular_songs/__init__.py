"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Construct core Flask application."""
    flask_app = Flask(__name__, instance_relative_config=False)
    flask_app.config.from_object('config.Config')

    with flask_app.app_context():
        # Import Flask routes
        from .interface import controller

        from .interface.dashboard import create_dashboard
        flask_dash_app = create_dashboard(flask_app)

        return flask_dash_app
