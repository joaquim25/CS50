# Songs
This project involves writing SQL queries to analyze data about songs and their artists stored in the SQLite database, songs.db. The database contains data on the top 100 streamed songs on Spotify in 2018. This project was completed as part of the CS50 course offered by Harvard University.

## Getting Started
To begin, run the command sqlite3 songs.db in your terminal to start querying the database. Once in the sqlite3 prompt, enter .schema to view the CREATE TABLE statements for each table in the database.

## Background
The songs.db database consists of two tables, songs and artists. Each song has a name, an artist_id (corresponding to the id of the artist of the song), and values for the danceability, energy, key, loudness, speechiness, valence, tempo, and duration of the song (measured in milliseconds). Every artist has an id and a name.

## Implementation Details
This project consists of eight SQL queries, each written to answer a specific question about the data in the songs.db database. Below are the SQL queries and the questions they answer:

```
SELECT name FROM songs;
``` 
List the names of all songs in the database.
```
SELECT name FROM songs ORDER BY tempo;
``` 
List the names of all songs in increasing order of tempo.
```
SELECT name FROM songs ORDER BY duration_ms DESC LIMIT 5;
```
List the names of the top 5 longest songs, in descending order of length.
```
SELECT name FROM songs WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75; 
```
List the names of any songs that have danceability, energy, and valence greater than 0.75.
```
SELECT AVG(energy) FROM songs;
```
Return the average energy of all the songs.
```
SELECT s.name FROM songs s JOIN artists a ON s.artist_id = a.id WHERE a.name = 'Post Malone'; 
```
List the names of songs that are by Post Malone.
```
SELECT AVG(s.energy) as average_energy FROM songs s JOIN artists a ON s.artist_id = a.id WHERE a.name = 'Drake';
```
Return the average energy of songs that are by Drake.
```
SELECT name FROM songs WHERE name LIKE '%feat.%';
```
List the names of the songs that feature other artists.


## Example Usage
To run these SQL queries, navigate to the directory containing songs.db and enter the command sqlite3 songs.db. Once in the sqlite3 prompt, copy and paste the desired query from the answers.txt file into the prompt and press enter. The results of the query will be displayed in the terminal window.

### Author
This project was completed by Joaquim Luzia.

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
