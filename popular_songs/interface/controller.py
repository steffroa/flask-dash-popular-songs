import os
import pandas as pd
from flask import send_from_directory, abort

from factory import factory
from flask import current_app as app


class RestController:
    def __init__(self):
        self.music_provider = factory.get_music_provider()
        self.application_service = factory.get_application_service()

    def get_csv(self):
        """
        Generates a csv file with today's popular songs
        :return: CSV File
        """
        global_songs = self.application_service.get_global_popular_songs()
        songs_dict = {
            'country': [],
            'name': [],
            'artist': [],
            'energy': [],
            'popularity': [],
            'danceability': [],
            'acousticness': [],
            'liveness': [],
            'loudness': [],
            'valence': [],
            'speechiness': [],
            'instrumentalness': []
        }

        for c in global_songs:
            for s in global_songs[c]:
                songs_dict['country'].append(c)
                songs_dict['name'].append(s.name)
                songs_dict['artist'].append(s.artist_name)
                songs_dict['energy'].append(s.energy)
                songs_dict['popularity'].append(s.popularity)
                songs_dict['danceability'].append(s.danceability)
                songs_dict['acousticness'].append(s.acousticness)
                songs_dict['liveness'].append(s.liveness)
                songs_dict['loudness'].append(s.loudness)
                songs_dict['valence'].append(s.valence)
                songs_dict['speechiness'].append(s.speechiness)
                songs_dict['instrumentalness'].append(s.instrumentalness)

        df = pd.DataFrame.from_dict(songs_dict)
        filename = 'global_songs.csv'
        csv_path = os.path.join(app.config.get('CLIENT_CSV'), filename)
        df.to_csv(csv_path, index=False, header=True)

        try:
            return send_from_directory(app.config.get('CLIENT_CSV'), filename, as_attachment=True)
        except FileNotFoundError:
            abort(404)


@app.route('/songs', methods=['GET'])
def get_song():
    controller = RestController()
    return controller.get_csv()

