# Mario
This program is a C implementation of the iconic pyramids of blocks that Mario must hop over in the first level of Nintendo's Super Mario Brothers. The program prompts the user to enter the height of the pyramids, between 1 and 8 inclusive, and then outputs the pyramids using hashes (#) for the bricks.

## Usage
To run the program, navigate to the directory where the population.c file is located in your terminal window, then compile and execute the program using the following commands:
```
$ make mario
$ ./mario
```
The program will prompt the user to enter the height of the pyramids. The user should enter a positive integer between 1 and 8, inclusive. If the user enters an invalid input, the program will re-prompt them until they enter a valid input.

Once the user enters a valid height, the program will output the pyramids with the specified height using hashes (#) for the bricks. Each hash is taller than it is wide, so the pyramids themselves will also be taller than they are wide. The width of the gap between adjacent pyramids is equal to the width of two hashes, irrespective of the pyramids' heights.

## Example Usage
```
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```
```
$ ./mario
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

## Testing
To test this program, you can try entering different inputs such as negative numbers, zero, letters, and words. The program should re-prompt you until you enter a valid input. You can also try entering integers between 1 and 8, and verify that the program outputs the pyramids correctly.

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
