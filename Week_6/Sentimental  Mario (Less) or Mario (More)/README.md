# Mario

## Getting started
To use this program, you will need to have Python 3 installed on your computer. You will also need to have the CS50 library installed, which you can install using pip by running pip install cs50.

## Background
This program is a Python implementation of the popular problem set from Harvard's CS50 course, in which you create half-pyramids using hashes (#) for blocks. The user is prompted for the height of the half-pyramids, and the program generates the desired half-pyramids with the specified height.

## Implementation details
The program prompts the user for the height of the half-pyramids using the get_int function from the CS50 library. The program then uses a while loop to validate that the height is between 1 and 8, inclusive. If the height is not valid, the program will reprompt the user for the height.

Once a valid height has been provided, the program uses a for loop to generate the desired half-pyramids. The program uses string multiplication to generate the correct number of spaces and hashes for each row of the half-pyramids.

## Example usage
```
$ python mario.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

## Author
Joaquim Luzia

## Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
