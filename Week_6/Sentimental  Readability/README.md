# Readability
readability.py - A Python program to compute the reading grade level of a given text using the Coleman-Liau formula.

## Getting started
To run this program, you must have Python 3 installed on your computer.

Download the readability.py file.
Open a terminal or command prompt and navigate to the directory where the readability.py file is saved.
Run the program by typing python readability.py.
Follow the prompts to enter the text to be analyzed.
The program will output the reading grade level of the text.

## Background
The Coleman-Liau formula is a readability test designed to measure the difficulty of reading and understanding a particular text. It computes the grade level required to understand the text based on the average number of letters and sentences per 100 words in the text.

## Implementation details
This program uses the following functions to count the number of letters, words, and sentences in the text:

- count_letters(text) - returns the number of letters in the text.
- count_words(text) - returns the number of words in the text.
- count_sentences(text) - returns the number of sentences in the text.

The main function prompts the user to input the text to be analyzed and then computes the reading grade level using the Coleman-Liau formula.

If the computed grade level is less than 1, the program outputs "Before Grade 1". If the grade level is 16 or higher, the program outputs "Grade 16+". Otherwise, the program outputs "Grade X", where X is the rounded grade level computed by the formula.

## Example usage
```
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
