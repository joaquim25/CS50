# Colorize

## Getting started
To execute the program, type:

```
$ make colorize
$ ./colorize infile outfile
```
where infile is the name of the BMP image you want to process and outfile is the name of the new BMP image you are creating.

## Background
This program was completed as part of the CS50 course offered by Harvard University. The goal of the program is to change all the black pixels in an image to a color of your choosing.

## Implementation details
The colorize function in helpers.c takes in the image's height, width, and a two-dimensional array of pixels as input parameters. In the current implementation, it changes all black pixels in the image to a shade of green.

The colorize function is then called in the main function in colorize.c. The program reads in the input BMP file, checks if the format is supported, allocates memory for the image, reads in the pixel data, calls the colorize function, and writes the new BMP file to disk.

Example usage
Suppose we have an input BMP image smiley.bmp that we want to colorize and save as out.bmp. We can do this by typing:

```
./colorize smiley.bmp out.bmp
```

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
