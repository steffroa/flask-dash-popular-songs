import sqlite3
from popular_songs.domain.repository import CountryRepository
from popular_songs.domain.models import Country


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
