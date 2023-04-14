# Population Growth
This program calculates how long it takes for a population to reach a particular size based on birth and death rates.

## Getting Started
To run the program, navigate to the directory where the population.c file is located in your terminal window, then compile and execute the program using the following commands:

```
$ make population
$ ./population
```

You will be prompted to enter a starting population size and an ending population size. If the starting population is less than 9, you will be re-prompted until a valid number is entered. If the ending population is less than the starting population, you will also be re-prompted until a valid number is entered.

After valid input is entered, the program will calculate and output the number of years it takes for the population to reach the specified size.

## Background
Assuming a starting population of n llamas, each year n / 3 new llamas are born, and n / 4 llamas pass away.

For example, if we were to start with n = 1200 llamas, then in the first year, 1200 / 3 = 400 new llamas would be born and 1200 / 4 = 300 llamas would pass away. At the end of that year, we would have 1200 + 400 - 300 = 1300 llamas.

## Implementation Details
The get_start_size() and get_end_size() functions prompt the user to input the starting and ending population sizes respectively. They use a while loop to continue prompting the user until a valid number is entered.

The calculate_years() function calculates the number of years required for the population to reach the specified size using a while loop.

The main() function calls the above functions and outputs the result to the console.

## Example Usage
```
$ make population
$ ./population
Enter starting population size: 5
Starting population size must be at least 9. Please try again.
Enter starting population size: 10
Enter ending population size: 100
Years: 24
``` 

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
