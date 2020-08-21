from datetime import date
from decimal import Decimal


class Country:
    def __init__(self, id: int, iso_code: str, name: str):
        self.id = id
        self.iso_code = iso_code
        self.name = name


class FeaturedSongs:
    def __init__(self, id: int, country_id: int, ddate: date):
        self.id = id
        self.country_id = country_id
        self.date = ddate


class Song:
    def __init__(self, music_provider_id: str, name: str, artist_name: str, energy: Decimal,
                 popularity, danceability: Decimal, acousticness: Decimal, liveness: Decimal,
                 loudness: Decimal, valence: Decimal, speechiness: Decimal, instrumentalness: Decimal):
        self.music_provider_id = music_provider_id
        self.name = name
        self.artist_name = artist_name
        self.energy = energy
        self.popularity = popularity
        self.danceability = danceability
        self.acousticness = acousticness
        self.liveness = liveness
        self.loudness = loudness
        self.valence = valence
        self.speechiness = speechiness
        self.instrumentalness = instrumentalness
