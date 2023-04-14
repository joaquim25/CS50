#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int row = 0; row < height; row++)
    {
        for (int spaces = height - row - 1; spaces > 0; spaces--) //print left spaces
        {
            printf(" ");
        }
        for (int hash = 0; hash <= row; hash++)  //print right hashes
        {
            printf("#");
        }
        printf("  ");   //print middle break
        for (int hash = 0; hash <= row; hash++) //print left hashes
        {
            printf("#");
        }
        printf("\n");
    }
}