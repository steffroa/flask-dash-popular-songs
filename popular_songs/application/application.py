from popular_songs.application.music_provider import MusicProvider
from popular_songs.domain.repository import CountryRepository


class ApplicationService:
    def __init__(self, music_provider: MusicProvider, country_repository: CountryRepository):
        self.music_provider = music_provider
        self.country_repository = country_repository

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
