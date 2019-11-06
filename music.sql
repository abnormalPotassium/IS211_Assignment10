DROP SCHEMA if exists music;
CREATE SCHEMA music;
USE music;

CREATE TABLE artist
( 
	artist_name varchar(100) PRIMARY KEY 
);

CREATE TABLE album
(
    album_name varchar(100) PRIMARY KEY,
    artist_name varchar(100) ,
    FOREIGN KEY (artist_name)
        REFERENCES artist(artist_name) 
);

CREATE TABLE song
(
    song_name varchar(100) PRIMARY KEY,
    album_name varchar(100),
    track_number INT,
    song_length INT,
    FOREIGN KEY (album_name)
        REFERENCES album(album_name)
);