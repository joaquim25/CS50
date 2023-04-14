# Tournament Simulator
## Getting Started
To use this program, you will need a CSV file with a list of teams and their ratings. You can run the program by running python tournament.py FILENAME on the command line, where FILENAME is the name of the CSV file containing the list of teams.

## Background
This program simulates a sports tournament using the Elo rating system. It calculates each team's probability of winning a game based on their rating, and uses that to simulate games between teams. It then simulates the tournament by simulating games between pairs of teams until only one team remains.

## Implementation Details
The program reads the list of teams and their ratings from the CSV file provided, and adds each team to a list of teams. It then simulates N tournaments, where N is a constant set to 100, and keeps track of how many times each team wins in a dictionary called counts.

The program uses the Elo rating system to simulate games between teams. The probability that a team with a higher rating will win a game against a team with a lower rating is calculated using the following formula:

probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))

The program then uses the random module to generate a random number between 0 and 1, and determines the winner of the game based on whether this number is less than the calculated probability.

The program then simulates the tournament by repeatedly simulating rounds, where each round consists of games between pairs of teams. The winners of each game go on to the next round, until only one team remains.

## Example Usage
Suppose we have a CSV file called teams.csv containing the following:

```
team,rating
Uruguay,2100
Portugal,2000
Spain,1900
Germany,1800
```
To run the program on this file, we would run the following command:

```
python tournament.py teams.csv
```
This would output the following:

```
Uruguay: 42.0% chance of winning
Portugal: 31.0% chance of winning
Spain: 18.0% chance of winning
Germany: 9.0% chance of winning
```
This means that Uruguay has a 42% chance of winning the tournament, Portugal has a 31% chance, Spain has an 18% chance, and Germany has a 9% chance.

### Author
Joaquim Luzia.

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
