# Credit Card Validator
This is a program written in C language that validates a credit card number using Luhn's Algorithm. It prompts the user to input a credit card number and reports whether it is a valid American Express, MasterCard, or Visa card number, or invalid.

## Luhn's Algorithm
Luhn's algorithm is a simple checksum formula used to validate various identification numbers, including credit card numbers. According to Luhn's algorithm, you can determine if a credit card number is valid as follows:

1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
2. Add the sum to the sum of the digits that weren’t multiplied by 2.
3. If the total’s last digit is 0, the number is valid.

## Implementation Details
The program is implemented in the credit.c file located in the credit directory. To compile the program, use the following command in the terminal:

To run the program, use the following command:
```
make credit
./credit
```

The program prompts the user to input a credit card number, which must be entirely numeric and devoid of hyphens or leading zeros. It then checks whether the number is a valid American Express, MasterCard, or Visa card number, or invalid, and prints the result via printf. The last line of output must be AMEX\n or MASTERCARD\n or VISA\n or INVALID\n, nothing more, nothing less. To get user input, the program uses get_long from the CS50 library.

The program is tested with various inputs, including valid and invalid credit card numbers. Here are some credit card numbers that PayPal recommends for testing:

:arrow_forward: American Express: 378282246310005, 371449635398431

:arrow_forward: MasterCard: 5555555555554444, 5105105105105100

:arrow_forward: Visa: 4012888888881881, 4111111111111111

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
