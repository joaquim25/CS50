# Speller
## Getting Started
This program implements a spell-checker in C using a hash table. It loads a dictionary of words into memory and then checks the spelling of words in a given text file against the loaded dictionary.

To use this program, you need to have a dictionary file and a text file to check. You can run the program from the command line using the following command:

```
$ make speller
$ ./speller dictionary text
```
## Background
This program was completed as part of the CS50 course offered by Harvard University.

## Implementation Details
The program uses a hash table to store the words from the dictionary. Each node in the hash table contains a word and a pointer to the next node in the linked list. The hash function used is a simple hash function that takes each character of the word and adds it to the hash value.

The load function reads in each word from the dictionary file, computes its hash value, and adds it to the hash table. The check function looks up a word in the hash table by computing its hash value and then iterating through the linked list at that index until the word is found or the end of the list is reached. The size function simply returns the number of words in the hash table. The unload function frees the memory used by the hash table and all of its nodes.

## Example Usage
Here is an example of how to use this program:
```
$ ./speller dictionaries/small text
```
```
MISSPELLED WORDS

surpise
writting
```
This example runs the program on the text file using the small dictionary. The program reports that there are two misspelled words in the text file, and it also reports the number of words in the dictionary and the text file, as well as the time it took to load, check, size, and unload the hash table.

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
