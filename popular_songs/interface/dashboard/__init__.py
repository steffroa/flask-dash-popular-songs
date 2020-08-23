import os
import dash
import dash_bootstrap_components as dbc
from datetime import date

from .data import DashController
from .layout import get_app_layout
from .callback import init_callback


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets=[
            dbc.themes.BOOTSTRAP
        ]
    )

    # Create Dash Layout
    dash_app.layout = get_app_layout()

    init_callback(dash_app)

    return dash_app.server
