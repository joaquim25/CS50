# Scrabble-like Game
This program is a simple implementation of a Scrabble-like game. Two players enter their words, and the program determines the winner based on the point values assigned to each letter of the alphabet.

## Dependencies
The program requires the following dependencies:

:arrow_forward: C Standard Library: stdio.h, string.h, ctype.h

:arrow_forward: CS50 Library: cs50.h

## Getting Started
To run the program, navigate to the directory where the scrabble.c file is located in your terminal window, then compile and execute the program using the following commands:
```
$ make scrabble
$ ./scrabble
```
Enter the word for Player 1 when prompted.
Enter the word for Player 2 when prompted.
The program will determine the winner based on the point values of the entered words.

## How it Works
The program uses the POINTS array, which stores the point values of each letter of the alphabet, to compute the scores of the entered words. The compute_score() function takes a string as input and returns the score for the string argument. Characters that are not letters are given zero points, and uppercase and lowercase letters are given the same point values.

In main(), the program prompts the two players for their words using the get_string() function. These values are stored inside variables named word1 and word2. The program then computes the scores for the entered words using compute_score() and compares them to determine the winner. If the scores are tied, the program prints "Tie!".

### Note
This implementation does not check if the entered words are in the dictionary, which is a requirement in the actual game of Scrabble.

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
