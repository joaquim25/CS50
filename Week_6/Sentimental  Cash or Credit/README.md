# Credit

## Getting Started
To run the program, you need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/
Also, you need to have the CS50 library installed. You can install it using the command: pip install cs50

## Background
This program is a solution to Problem Set 1 of CS50 course offered by Harvard University. The program checks whether a credit card number is valid or not. The program identifies the credit card company (American Express, MasterCard or Visa) based on the credit card number and uses the Luhn's algorithm to check the validity of the number.

## Implementation Details
The program prompts the user to enter a credit card number and then identifies the credit card company (if possible). Then, it checks the validity of the credit card number using the Luhn's algorithm. Finally, it prints the result (credit card company or "INVALID").

## Example Usage
To run the program, open the terminal and navigate to the directory where the program is located. Then, type the following command and press Enter:

```
python credit.py
```
Example:

```
$ python credit.py
Number: 378282246310005
AMEX
```

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
