# DNA Identification Program

## Getting Started:
To run this program, you need to have Python installed on your computer. The program requires two command-line arguments: the name of a CSV file containing the STR counts for a list of individuals, and the name of a text file containing the DNA sequence to identify. If the incorrect number of command-line arguments is provided, the program will print an error message.

## Background:
This program is designed to identify to whom a sequence of DNA belongs by comparing the STR (short tandem repeat) counts of the given DNA sequence with those in a CSV file containing the STR counts for a list of individuals. An STR is a DNA sequence that consists of a short pattern repeated multiple times.

## Implementation Details:
The program reads the CSV file and the DNA sequence file into memory. For each STR in the CSV file, the program uses the longest_match function to find the longest consecutive run of the STR in the DNA sequence. The program then compares the STR counts obtained from the DNA sequence with those of each individual in the CSV file. If there is an exact match, the program prints the name of the matching individual. Otherwise, the program prints "No match".

## Example Usage:
Suppose you have a CSV file called "people.csv" and a text file called "dna.txt" containing the DNA sequence to identify. To run the program, open the terminal or command prompt and navigate to the directory containing the program and the files. Then run the following command:
python dna.py people.csv dna.txt

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
