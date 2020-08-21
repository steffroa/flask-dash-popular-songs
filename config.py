from os import environ, path

BASE_DIR = path.abspath(path.dirname(__file__))


class Config:
    """Flask configuration variables."""

    # General Config
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    CLIENT_CSV = path.join(BASE_DIR, 'popular_songs/static', 'client', 'csv')
