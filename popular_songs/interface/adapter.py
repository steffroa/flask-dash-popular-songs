from popular_songs.domain.models import Song


class SpotifySongAdapter:

    @staticmethod
    def get_artists(artists_data: dict) -> str:
        artists = ''
        for a in artists_data:
            if artists:
                artists += ', {}'.format(a.get('name'))
            else:
                artists = a.get('name')

        return artists

    def to_song_model(self, track_data: dict, audio_features_data: dict) -> Song:
        spotify_id = track_data.get('id')
        name = track_data.get('name')
        artists = self.get_artists(track_data.get('artists'))
        energy = audio_features_data.get('energy')
        danceability = audio_features_data.get('danceability')
        popularity = track_data.get('popularity')
        acousticness = audio_features_data.get('acousticness')
        liveness = audio_features_data.get('liveness')
        loudness = audio_features_data.get('loudness')
        valence = audio_features_data.get('valence')
        speechiness = audio_features_data.get('speechiness')
        instrumentalness = audio_features_data.get('instrumentalness')

        return Song(spotify_id, name, artists, energy, popularity, danceability, acousticness,
                    liveness, loudness, valence, speechiness, instrumentalness)
