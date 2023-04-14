# Image Manipulation

## Getting started
This program is designed to manipulate images in several ways, including grayscale, sepia, reflection, and blurring. To run this program, you must have a C compiler installed on your computer.

## Background
This program was completed as part of the CS50 course offered by Harvard University. The purpose of this program is to demonstrate how to manipulate images using C.

## Implementation details
The program consists of four functions:

1. grayscale: Converts an image to grayscale.
2. sepia: Converts an image to sepia.
3. reflect: Reflects an image horizontally.
4. blur: Blurs an image.

Each function takes in the height and width of an image and a 2D array of RGBTRIPLE structs, which represent the pixels in the image.

- grayscale converts each pixel in the image to grayscale by taking the average value of the red, green, and blue color values and setting each color value to that average value.
- sepia converts each pixel in the image to sepia by applying a formula that changes the red, green, and blue color values to sepia equivalents.
- reflect reflects each pixel in the image horizontally by swapping each pixel with its corresponding pixel on the opposite side of the image.
- blur blurs each pixel in the image by taking the average of the color values of each pixel and its surrounding pixels. The blurred color values are then applied to each pixel.

## Example usage
To use this program, include the helpers.h header file in your C code and call the desired function, passing in the height, width, and 2D array of RGBTRIPLE structs representing the image.

Example:
```
#include <stdio.h>
#include <stdlib.h>
#include "helpers.h"

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./filter filter_name infile outfile\n");
        return 1;
    }

    char *filter_name = argv[1];
    char *infile = argv[2];
    char *outfile = argv[3];

    // Read image
    RGBTRIPLE (*image)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (image == NULL)
    {
        fprintf(stderr, "Not enough memory to store image.\n");
        return 2;
    }
    if (read_image(infile, height, width, image))
    {
        return 3;
    }

    // Manipulate image
    if (strcmp(filter_name, "grayscale") == 0)
    {
        grayscale(height, width, image);
    }
    else if (strcmp(filter_name, "sepia") == 0)
    {
        sepia(height, width, image);
    }
    else if (strcmp(filter_name, "reflect") == 0)
    {
        reflect(height, width, image);
    }
    else if (strcmp(filter_name, "blur") == 0)
    {
        blur(height, width, image);
    }

    // Write image
    if (write_image(outfile, height, width, image))
    {
        return 4;
    }

    return 0;
}
```

Author
Joaquim Luzia

Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
