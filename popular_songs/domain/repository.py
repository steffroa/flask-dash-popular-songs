from abc import ABC, abstractmethod
from .models import Country


class CountryRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_code(self):
        pass

    @abstractmethod
    def get_by_id(self, id) -> Country:
        pass

    @abstractmethod
    def get_by_name(self, name) -> Country:
        pass


class FeaturedSongsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_date(self, date):
        pass

    @abstractmethod
    def get_by_country(self):
        pass

    @abstractmethod
    def save_features_songs(self, country_id, date):
        pass


class SongRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_music_provider_id(self):
        pass

    @abstractmethod
    def get_by_featured_songs_id(self, featured_songs_id):
        pass

    @abstractmethod
    def save_song(self, obj, featured_song_id):
        pass
