# Recover JPEGs from a Forensic Image
## Getting Started
To use this program, you must have a forensic image from which to recover JPEG files. The program must be executed with exactly one command-line argument, which is the name of the forensic image.
```
$ make population
$ ./population image-name
```
If you do not provide the correct number of arguments, the program will remind you of the correct usage and exit.

If the forensic image cannot be opened for reading, the program will inform you and exit.

The program will generate JPEG files from the forensic image, named with a three-digit decimal number starting with 000 for the first image and counting up.

## Background
This program is part of the CS50 course offered by Harvard University. The goal of the program is to recover JPEGs from a forensic image.

## Implementation Details
The program reads the forensic image in chunks of 512 bytes and checks if the first four bytes of each chunk are those of a JPEG file. If so, the program writes the chunk to a new file named with a three-digit decimal number, starting with 000 for the first image and counting up. If the chunk is not the start of a new JPEG file, the program writes the chunk to the current file.

The program uses malloc to allocate memory for the new files, but ensures that no memory leaks occur.

Example Usage
```
$ ./recover card.raw
```

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
