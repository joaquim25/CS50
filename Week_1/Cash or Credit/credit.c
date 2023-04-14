#include <stdio.h>
#include <string.h>

// Function to validate credit card number using Luhn's Algorithm
int validate_cc(char *cc_number)
{
    int sum = 0;
    int len = strlen(cc_number);
    int is_second = 0;

    for (int i = len - 1; i >= 0; i--)
    {
        int digit = cc_number[i] - '0';

        if (is_second == 1)
        {
            digit = digit * 2;
        }

        sum += digit / 10 + digit % 10;

        is_second = !is_second;
    }

    return sum % 10 == 0;
}

// Function to check card type based on starting digits and length
int check_card_type(char *cc_number)
{
    int len = strlen(cc_number);
    char first_two_digits[3];

    snprintf(first_two_digits, sizeof(first_two_digits), "%c%c", cc_number[0], cc_number[1]);

    if (cc_number[0] == '4' && (len == 13 || len == 16))
    {
        printf("VISA\n");
        return 0;
    }
    else if ((strcmp(first_two_digits, "34") == 0 || strcmp(first_two_digits, "37") == 0) && len == 15)
    {
        printf("AMEX\n");
        return 0;
    }
    else if ((strcmp(first_two_digits, "51") == 0 || strcmp(first_two_digits, "52") == 0 || strcmp(first_two_digits, "53") == 0
              || strcmp(first_two_digits, "54") == 0 || strcmp(first_two_digits, "55") == 0) && len == 16)
    {
        printf("MASTERCARD\n");
        return 0;
    }
    else
    {
        printf("INVALID\n");
        return 0;
    }
}

int main(void)
{
    char cc_number[20];

    printf("Enter credit card number: ");
    scanf("%s", cc_number);

    if (validate_cc(cc_number))
    {
        check_card_type(cc_number);
        return 0;
    }
    else
    {
        printf("INVALID\n");
        return 0;
    }

}