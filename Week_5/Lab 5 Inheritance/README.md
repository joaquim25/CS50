# Genetic Inheritance of Blood Type
## Getting Started
To use this program, simply compile it and run it. The program will create a family tree with a specified number of generations, and assign blood type alleles to each family member. The oldest generation will have alleles assigned randomly to them.

## Background
This program simulates the genetic inheritance of blood type using a struct called person. Each person has two parents and two alleles. The program creates a family with a specified number of generations and assigns alleles to each family member. The oldest generation has alleles assigned randomly to them, and younger generations inherit one allele from each parent.

## Implementation Details
The create_family function takes an integer generations as input and allocates memory for one person for each member of the family of that number of generations, returning a pointer to the person in the youngest generation. Each person has alleles assigned to them, with the oldest generation having alleles randomly chosen by calling the random_allele function, and younger generations inheriting one allele (chosen at random) from each parent. Each person also has parents assigned to them, with the oldest generation having both parents set to NULL, and younger generations having parents be an array of two pointers, each pointing to a different parent.

The print_family function prints each family member and their alleles, along with their generation. The function uses indentation to make it easy to see the family tree structure.

## Example Usage
To create a family with three generations and print the family tree of blood types, run the program:

```
$ make inheritance
$ ./inheritance
```
The program will output something like this:
```
Child (Generation 0): blood type AB
    Parent (Generation 1): blood type Bb
        Grandparent (Generation 2): blood type aa
        Grandparent (Generation 2): blood type AB
    Parent (Generation 1): blood type AB
        Grandparent (Generation 2): blood type Bb
        Grandparent (Generation 2): blood type AB
```

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
