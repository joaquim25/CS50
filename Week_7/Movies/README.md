# Movies

## Getting Started
This project is about writing SQL queries to extract information from a SQLite database called "movies.db", which stores data from IMDb about movies, their directors, actors, and ratings. To start, run the command sqlite3 movies.db in a terminal window to connect to the database. You can then begin executing queries on the database.

## Background
The "movies.db" database consists of several tables, including the "movies" table which has columns for movie ID, title, and release year. Similarly, the "people" table has columns for person ID, name, and birth year. The "ratings" table stores movie ratings, with a column for the movie ID and columns for the rating and number of votes. The "stars" and "directors" tables match people to the movies in which they acted or directed.

## Implementation Details
For this project, I wrote some SQL queries to extract information from the database by selecting data from one or more of these tables. Each problem requires a single SQL query to output the results specified by the problem. Nested queries could be used, but it should be assumed that the IDs of any particular movies or people may differ. Each query should only return the data necessary to answer the question.

## Example Usage
The following are examples of the SQL queries that will be written for this project:

To list the titles of all movies released in 2008:
```
SELECT title FROM movies WHERE year = 2008;
```
To determine the birth year of Emma Stone:
```
SELECT birth FROM people WHERE name = 'Emma Stone';
```
To list the titles of all movies with a release date on or after 2018, in alphabetical order:
```
SELECT title FROM movies WHERE year >= 2018 ORDER BY title ASC;
```
To determine the number of movies with an IMDb rating of 10.0:
```
SELECT COUNT(*) FROM ratings WHERE rating = 10.0;
```
To list the titles and release years of all Harry Potter movies, in chronological order:
```
SELECT title, year FROM movies WHERE title LIKE 'Harry Potter%' ORDER BY year ASC;
```
To determine the average rating of all movies released in 2012:
```
SELECT AVG(rating) FROM ratings WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012);
```
To list all movies released in 2010 and their ratings, in descending order by rating:
```
SELECT title, rating FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE year = 2010 AND rating IS NOT NULL ORDER BY rating DESC, title ASC;
```
To list the names of all people who starred in Toy Story:
```
SELECT name FROM people JOIN stars ON people.id = stars.person_id JOIN movies ON movies.id = stars.movie_id WHERE movies.title = 'Toy Story';
```
To list the names of all people who starred in a movie released in 2004, ordered by birth year:
```
SELECT name FROM people JOIN stars ON people.id = stars.person_id JOIN movies ON movies.id = stars.movie_id WHERE movies.year = 2004 AND people.birth IS NOT NULL ORDER BY birth ASC;
```
To list the names of all people who both directed and starred in the same movie:
```
SELECT DISTINCT name FROM people JOIN directors ON people.id = directors.person_id JOIN stars ON people.id = stars.person_id WHERE directors.movie_id = stars.movie_id;
```

### Author
This project was created by Joaquim Luzia.

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
