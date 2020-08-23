import pandas as pd

from factory import factory


class DashController:
    def __init__(self, sdate: str):
        self.application_service = factory.get_application_service()
        self.date = sdate

    def create_dataframe(self):
        popular_songs = self.application_service.get_popular_songs_by_date(self.date)
        songs_dict = {
            'date': [],
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

        for c in popular_songs:
            for s in popular_songs[c]:
                songs_dict['date'].append(self.date)
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

        return pd.DataFrame.from_dict(songs_dict)

    @staticmethod
    def get_kpi_from_df(df):
        return df.groupby('country').mean()[['energy', 'danceability', 'acousticness',
                                             'liveness', 'valence', 'speechiness']]

    @staticmethod
    def get_df_from_csv(file_path):
        return pd.read_csv(file_path)
