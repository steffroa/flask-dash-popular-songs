from datetime import date, datetime

from popular_songs.application.music_provider import MusicProvider
from popular_songs.domain.repository import CountryRepository
from popular_songs.domain.repository import FeaturedSongsRepository
from popular_songs.domain.repository import SongRepository


class ApplicationService:
    def __init__(self, music_provider: MusicProvider, country_repository: CountryRepository,
                 featured_songs_repository: FeaturedSongsRepository, song_repository: SongRepository):
        self.music_provider = music_provider
        self.country_repository = country_repository
        self.featured_songs_repository = featured_songs_repository
        self.song_repository = song_repository

    def get_global_popular_songs(self) -> dict:
        """
        Returns popular songs by country
        :return: dict[country_name] = list(songs)
        """
        countries = self.country_repository.get_all()
        country_songs = {}
        for country in countries:
            country_songs[country.name] = self.music_provider.get_popular_songs(country)
        return country_songs

    def get_popular_songs_by_date(self, sdate: str) -> dict:
        featured_songs = self.featured_songs_repository.get_by_date(sdate)
        date_is_today = datetime.strptime(sdate, '%Y-%m-%d').date() == date.today()
        country_songs = {}

        for fs in featured_songs:
            country = self.country_repository.get_by_id(fs.country_id)
            if country:
                country_songs[country.name] = self.song_repository.get_by_featured_songs_id(fs.id)

        if not country_songs and date_is_today:
            country_songs = self.get_global_popular_songs()
            for country, songs in country_songs.items():
                self.save_popular_songs(sdate, country, songs)

        return country_songs

    def save_popular_songs(self, ddate, country_name, songs):
        country = self.country_repository.get_by_name(country_name)
        featured_songs_id = self.featured_songs_repository.save_features_songs(country.id, ddate)
        for s in songs:
            self.song_repository.save_song(s, featured_songs_id)
