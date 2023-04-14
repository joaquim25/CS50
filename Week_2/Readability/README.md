# Readability
The program is designed to compute the Coleman-Liau index of a given text input by the user.

## Getting Started
To run the program, navigate to the directory where the readability.c file is located in your terminal window, then compile and execute the program using the following commands:
```
$ make readability
$ ./readability
```

## Background
The Coleman-Liau index is a readability test designed to determine the grade level of a text by measuring the average number of letters and sentences per 100 words. This program prompts the user for a string of text, counts the number of letters, words, and sentences in the text, and then computes the grade level using the Coleman-Liau formula.

## Implementation Details
The "readability.c" file contains three functions:

count_letters(): takes a string of text as input and returns the number of letters in the text.
count_words(): takes a string of text as input and returns the number of words in the text.
count_sentences(): takes a string of text as input and returns the number of sentences in the text.

These functions are called by the main function which prompts the user for a string of text using get_string. The main function then uses the count_letters(), count_words(), and count_sentences() functions to count the number of letters, words, and sentences in the text. Finally, the main function computes the grade level using the Coleman-Liau formula and prints the result.

## Example Usage
Here is an example of how to use the "readability" program:

```
$ ./readability
Text: The quick brown fox jumps over the lazy dog.
Grade 3
```
In this example, the user has entered the text "The quick brown fox jumps over the lazy dog." The program has counted the number of letters, words, and sentences in the text and has computed the grade level to be 3.

Author
Joaquim Luzia.

Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
