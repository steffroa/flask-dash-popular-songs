from abc import ABC, abstractmethod


class CountryRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_code(self):
        pass


class FeaturedSongsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_date(self):
        pass

    @abstractmethod
    def get_by_country(self):
        pass


class SongRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_music_provider_id(self):
        pass
