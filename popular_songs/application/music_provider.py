from abc import ABC, abstractmethod
from popular_songs.domain.models import Country


class MusicProvider(ABC):

    @abstractmethod
    def get_popular_songs(self, country: Country):
        pass
