import sqlite3
from datetime import datetime

from popular_songs.domain.repository import CountryRepository
from popular_songs.domain.repository import FeaturedSongsRepository
from popular_songs.domain.repository import SongRepository
from popular_songs.domain.models import Country
from popular_songs.domain.models import FeaturedSongs
from popular_songs.domain.models import Song


class CountrySqliteRepository(CountryRepository):
    def __init__(self, database):
        self.db = database
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def get_all(self):
        self.cursor.execute('SELECT * FROM country')
        rows = self.cursor.fetchall()
        countries = []

        for r in rows:
            countries.append(Country(r['id'], r['iso_code'], r['name']))
        return countries

    def get_by_code(self):
        pass

    def get_by_id(self, id) -> Country:
        self.cursor.execute('SELECT * FROM country WHERE id = ?', (id,))
        record = self.cursor.fetchone()
        if record:
            return Country(record['id'], record['iso_code'],  record['name'])

    def get_by_name(self, name) -> Country:
        self.cursor.execute('SELECT * FROM country WHERE name = ?', (name,))
        record = self.cursor.fetchone()
        if record:
            return Country(record['id'], record['iso_code'], record['name'])


class FeaturedSongsSqliteRepository(FeaturedSongsRepository):
    def __init__(self, database):
        self.db = database
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def get_by_date(self, date):
        self.cursor.execute('SELECT * FROM featured_songs WHERE date = ?', (date,))
        rows = self.cursor.fetchall()
        featured_songs = []

        for r in rows:
            dd = datetime.strptime(r['date'], '%Y-%m-%d').date()
            featured_songs.append(FeaturedSongs(r['id'], r['country_id'], dd))
        return featured_songs

    def get_all(self):
        pass

    def get_by_country(self):
        pass

    def save_features_songs(self, country_id, date):
        self.cursor.execute('INSERT INTO featured_songs (date, country_id) VALUES (?, ?)',
                            (date, country_id))
        self.db.commit()
        return self.cursor.lastrowid


class SongSqliteRepository(SongRepository):
    def __init__(self, database):
        self.db = database
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def get_by_featured_songs_id(self, featured_songs_id):
        self.cursor.execute('SELECT song_id FROM country_songs WHERE featured_songs_id = ?', (featured_songs_id,))
        rows = self.cursor.fetchall()
        songs = []

        for r in rows:
            self.cursor.execute('SELECT * FROM song WHERE id = ?', (r['song_id'],))
            record = self.cursor.fetchone()
            if record:
                songs.append(Song(record['music_provider_id'], record['name'], record['artist_name'],
                                  record['energy'], record['popularity'], record['danceability'],
                                  record['acousticness'], record['liveness'], record['loudness'],
                                  record['valence'], record['speechiness'], record['instrumentalness']))
        return songs

    def get_all(self):
        pass

    def get_by_music_provider_id(self):
        pass

    def save_song(self, song, featured_song_id):
        song_values = (song.music_provider_id, song.name, song.artist_name, song.energy, song.popularity,
                       song.danceability, song.acousticness, song.liveness, song.loudness, song.valence,
                       song.speechiness, song.instrumentalness)
        self.cursor.execute('INSERT INTO song (music_provider_id, name, artist_name, energy, popularity,'
                            'danceability, acousticness, liveness, loudness, valence, speechiness,'
                            'instrumentalness) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', song_values)
        self.db.commit()

        self.cursor.execute('INSERT INTO country_songs (featured_songs_id, song_id) VALUES (?, ?)',
                            (featured_song_id, self.cursor.lastrowid))

        self.db.commit()
