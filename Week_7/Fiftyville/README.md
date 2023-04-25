# Fiftyville

This project is an exercise in which SQL queries must be written to solve a mystery. The mystery is related to the theft of the CS50 Duck in Fiftyville. The goal is to identify the thief, the city the thief escaped to, and the thief’s accomplice who helped them escape, given only the information contained in the provided SQLite database.

## Getting Started
To get started with this project, you need to have access to the fiftyville.db SQLite database provided by the Fiftyville authorities. The project consists of two main files: log.sql and answers.txt.

The log.sql file contains a log of all SQL queries that you run on the database. Each query is labeled with a comment (in SQL) describing why I ran the query and what information I was hoping to get out of it. This file should serve as evidence of the process used to identify the thief.

## Background
The CS50 Duck has been stolen! The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. The goal is to identify:

1. Who the thief is,
2. What city the thief escaped to.
3. Who the thief’s accomplice is who helped them escape.

All you know is that the theft took place on July 28, 2021, and that it took place on Humphrey Street.

The authorities have provided a SQLite database, fiftyville.db, which contains tables of data from around the town. You can query the database using SQL SELECT queries to access the data of interest to you.

## Implementation Details
To solve the mystery, various SQL queries were run on the database. The queries and the reasoning behind them are explained in the log.sql file. Here is a brief summary of the steps taken:

- Checked the description of the crime happened at the given location and time.
- Found the names of the witnesses from the interviews table and checked their interviews' transcripts.
- Found the names of the three witnesses from the list of names of people who gave interviews on July 28, 2021. Crime report said that the witnesses mentioned "bakery" in their transcripts. Also, ordered the results alphabetically by the names of witnesses.
- Found the account number of the person who withdrew money from the ATM on Leggett Street, and then - Found the names associated with the corresponding account numbers. These names were added to the suspect list.
- Found the information about the airport in Fiftyville that would be the origin of the thief's flight.
- Found the flights on July 29 from Fiftyville airport, ordered them by time, and identified the thief's flight and destination airport.
- Found the person who talked on the phone with Raymond and asked them to buy a flight ticket of the earliest flight on July 29, 2021.
- Once the mystery was solved, the answers were filled in the answers.txt file.

Example Usage
To solve the mystery, you can run the SQL queries in the log.sql file on the fiftyville.db database.

Here is an example of how to run the queries in the log file using the sqlite3 command-line tool:

```
sqlite3 fiftyville.db < log.sql
```

### Author
Joaquim Luzia.

Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
