# Plurality Vote Election Program
## Background
This program simulates a plurality vote election, where voters can choose one candidate to vote for, and the candidate with the most votes wins. The program takes in command-line arguments to specify the candidates running in the election, and prompts the user for the number of voters and each voter's choice. The program then outputs the winner (or winners) of the election.

## Getting Started
To run the program, open a terminal window and navigate to the directory where the program file is saved. Compile the program using the command:
```
$ make plurality
$ ./plurality
```
Follow the prompts to input the number of voters and each voter's choice.

## Implementation Details
The program defines a struct called candidate, with two fields: a string called name representing the candidate's name, and an int called votes representing the number of votes the candidate has.

The program uses a global array of candidates called candidates to store the candidates running in the election. The array is populated using the command-line arguments, and the number of candidates is stored in the global variable candidate_count.

The program includes two function prototypes: bool vote(string name) and void print_winner(void). The vote function takes a single argument, a string called name, representing the name of the candidate who was voted for. If name matches one of the names of the candidates in the election, then the function updates that candidate's vote total to account for the new vote and returns true. If name does not match the name of any of the candidates in the election, no vote totals change, and the function returns false.

The print_winner function prints out the name of the candidate who received the most votes in the election, and then prints a newline. If multiple candidates each have the maximum number of votes, the function outputs the names of each of the winning candidates, each on a separate line.

Example Usage
```
$ ./plurality Alice Bob
Number of voters: 3
Vote: Alice
Vote: Bob
Vote: Alice
Alice
```
```
$ ./plurality Alice Bob
Number of voters: 3
Vote: Alice
Vote: Charlie
Invalid vote.
Vote: Alice
Alice
```
```
$ ./plurality Alice Bob Charlie
Number of voters: 5
Vote: Alice
Vote: Charlie
Vote: Bob
Vote: Bob
Vote: Alice
Alice
Bob
```

### Author
Joaquim Luzia.

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
