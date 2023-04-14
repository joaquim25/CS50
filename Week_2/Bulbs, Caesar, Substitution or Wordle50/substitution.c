#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];
    int key_length = strlen(key);

    if (key_length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    for (int i = 0; i < key_length; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }

        for (int j = i + 1; j < key_length; j++)
        {
            if (tolower(key[i]) == tolower(key[j]))
            {
                printf("Key must not contain repeating characters.\n");
                return 1;
            }
        }
    }

    string plaintext = get_string("plaintext: ");
    int plaintext_length = strlen(plaintext);

    printf("ciphertext: ");
    for (int i = 0; i < plaintext_length; i++)
    {
        char c = plaintext[i];
        if (isalpha(c))
        {
            char key_char = islower(c) ? tolower(key[c - 'a']) : toupper(key[c - 'A']);
            printf("%c", key_char);
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
    return 0;
}