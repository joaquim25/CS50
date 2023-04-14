#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("What's your name? "); //Gets name of user
    printf("hello, %s\n", name); //Outputs string + name of prompt
}