# Popular Songs
Integrating dashboards in a web app using Flask and Dash 

## Project structure
```shell script
├── popular_songs
│   ├── __init__.py
│   ├── application
│   │   ├── application.py
│   │   ├── music_provider.py
│   │   └── spotify.py
│   ├── domain
│   │   ├── models.py
│   │   └── repository.py
│   ├── interface
│   │   ├── adapter.py
│   │   ├── controller.py
│   │   ├── dashboard
│   │   │   ├── __init__.py
│   │   │   ├── data.py
│   │   │   ├── callback.py
│   │   │   ├── layout.py
│   │   └── sqlite_repository.py
│   ├── static
│   │   └── client
│   │       └── csv
│   │           └── global_songs.csv
│   └── templates
├── config.py
├── factory.py
├── requirements.txt
├── README.md
├── schema.sql
└── wsgi.py
```
**Branches**:
* `flask-app`: Flask app before integration
* `dash-app`: Dash app before integration
* `master`: Integration = Flask as server and Dash as a module
## Setup
**Installation via `requirements.txt`**:

```shell script
$ git clone https://github.com/steffroa/flask-dash-popular-songs.git
$ cd flask-dash-popular-songs
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip install -r requirements.txt
$ flask run
```

**Environmental variables**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
* `POPULAR_SONGS_DB`: `popular_songs.db` path. 

Create an app on https://developers.spotify.com/. Add your new ID and SECRET to your environment:
* `SPOTIFY_CLIENT_ID`: Client ID from your Spotify app.
* `SPOTIFY_CLIENT_SECRET`: Client Secret from your Spotify app.