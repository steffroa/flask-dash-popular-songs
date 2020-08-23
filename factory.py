import os
import sqlite3

from popular_songs.application.music_provider import MusicProvider
from popular_songs.application.spotify import Spotify
from popular_songs.domain.repository import CountryRepository
from popular_songs.interface.sqlite_repository import CountrySqliteRepository
from popular_songs.application.application import ApplicationService
from popular_songs.interface.sqlite_repository import FeaturedSongsSqliteRepository
from popular_songs.interface.sqlite_repository import SongSqliteRepository


class ServiceFactory:
    """
    Dependency Injection Factory
    """
    def __init__(self):
        self.spotify_client_id = os.environ['SPOTIFY_CLIENT_ID']
        self.spotify_client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
        self.database = os.environ['POPULAR_SONGS_DB']

    def get_music_provider(self) -> MusicProvider:
        return Spotify(self.spotify_client_id, self.spotify_client_secret, 4)

    def get_database_connection(self):
        return sqlite3.connect(self.database)

    def get_country_repository(self) -> CountryRepository:
        return CountrySqliteRepository(self.get_database_connection())

    def get_featured_songs_repository(self):
        return FeaturedSongsSqliteRepository(self.get_database_connection())

    def get_song_repository(self):
        return SongSqliteRepository(self.get_database_connection())

    def get_application_service(self) -> ApplicationService:
        return ApplicationService(self.get_music_provider(),
                                  self.get_country_repository(),
                                  self.get_featured_songs_repository(),
                                  self.get_song_repository())


factory = ServiceFactory()
