import sqlite3
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from .music_provider import MusicProvider
from popular_songs.interface.adapter import SpotifySongAdapter
from popular_songs.domain.models import Country


class Spotify(MusicProvider):
    """
    Music Provider implementation for Spotify API
    """
    def __init__(self, client_id, client_secret, limit_songs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.limit_songs = limit_songs
        self.playlist_category = 'toplists'

    def get_client(self):
        auth_manager = SpotifyClientCredentials(client_id=self.client_id,
                                                client_secret=self.client_secret)
        return spotipy.Spotify(auth_manager=auth_manager)

    @staticmethod
    def get_country_playlist_id(iso_code):
        """
        Searches in country table the spotify's playlist id by iso_code
        :param iso_code: string
        :return: string
        """
        database = os.environ['POPULAR_SONGS_DB']
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT music_provider_id FROM country WHERE iso_code = ?", (iso_code,))
        record = cur.fetchone()
        if record:
            return record[0]
        return None

    def get_popular_songs(self, country: Country) -> list:
        songs = []
        adapter = SpotifySongAdapter()
        sp = self.get_client()
        playlist_id = self.get_country_playlist_id(country.iso_code)
        if playlist_id:
            tracks_response = sp.playlist_tracks(playlist_id, offset=0, fields='items.track.id,total',
                                                 additional_types=['track'])
            tracks_ids = tracks_response.get('items')
            for track in tracks_ids:
                try:
                    track_id = track['track']['id']
                except TypeError:
                    continue
                track_data = sp.track(track_id)
                track_audio_features = sp.audio_features(track_id)
                if track_audio_features and isinstance(track_audio_features, list):
                    track_audio_features = track_audio_features[0]
                songs.append(adapter.to_song_model(track_data, track_audio_features))

        return songs
