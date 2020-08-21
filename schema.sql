DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS featured_songs;
DROP TABLE IF EXISTS song;

CREATE TABLE country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    iso_code VARCHAR(2),
    music_provider_id TEXT
);

CREATE TABLE featured_songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    country_id INTEGER,
    FOREIGN KEY(country_id) REFERENCES country(id)
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    music_provider_id TEXT,
    name TEXT,
    artist_name TEXT,
    energy REAL,
    popularity REAL,
    danceability REAL,
    acousticness REAL,
    liveness REAL,
    loudness REAL,
    valence REAL,
    speechiness REAL,
    instrumentalness REAL
);

CREATE TABLE country_songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    featured_songs_id INTEGER REFERENCES featured_songs(id),
    song_id INTEGER REFERENCES song(id)
);
