# Tideman Voting Algorithm

## Getting started
This program simulates the Tideman voting algorithm. It takes the number of candidates as a command-line argument and prompts the user to enter the number of voters and their preferences. The program then computes the Tideman winner, i.e., the candidate who wins the election using the Tideman voting method, and outputs the name of the winner.

To run the program, use the following command:
```
$ make tideman
$ ./tideman [candidate1] [candidate2] ... [candidate9]
```

## Background
The Tideman voting algorithm is a ranked-pairs voting method used to elect a single winner from a set of candidates. It works by computing a "graph of the strongest paths" from each candidate to another candidate, and then finding the "source" of the graph, i.e., the candidate who has no other candidate ranked above them.

## Implementation details
The program is implemented in C and uses the CS50 library. The program first reads in the number of candidates, and then prompts the user to enter the number of voters and their preferences. The program then computes the Tideman winner using the following steps:

Record the preferences of each voter.
Generate a list of all pairs of candidates and their strength of victory.
Sort the pairs in decreasing order of strength of victory.
Lock in each pair in the order determined by the sort, unless doing so would create a cycle in the graph of locked-in pairs.
The winner is the candidate who is the source of the graph of locked-in pairs.

## Example usage
Suppose we have the following candidates: Alice, Bob, Charlie, and David. To run the program, we would enter the following command:

```
./tideman Alice Bob Charlie David
```
The program would then prompt us to enter the number of voters and their preferences:

```
Number of voters: 3
Rank 1: Alice
Rank 2: Charlie
Rank 3: Bob
Rank 1: Charlie
Rank 2: Bob
Rank 3: Alice
Rank 1: David
Rank 2: Charlie
Rank 3: Alice
```
The program would then output the name of the winner:

```
Winner: Charlie
```
### Author
Joaquim Luzia.

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
