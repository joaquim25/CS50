# Substitution Cipher Program
## Getting Started
This program implements a substitution cipher to encrypt messages. The user must provide a key when executing the program as a command-line argument. The key must be a string of 26 unique alphabetical characters. The program then prompts the user to enter the plaintext message they wish to encrypt. The program only encrypts alphabetical characters, preserving their case and the spaces and punctuation in the plaintext. The program then outputs the ciphertext.

To run the program, navigate to the directory containing the substitution.c file and run the following command:
```
$ make substitution
$ ./substitution key
```

## Background
A substitution cipher is a method of encrypting a message by replacing each letter in the plaintext with a different letter. The encryption is achieved by using a key, which is a mapping of each letter of the alphabet to a different letter. To decrypt the message, the receiver must know the key so that they can reverse the process of translating the ciphertext back into the original plaintext.

## Implementation Details
The substitution program accepts a single command-line argument, which is the key to use for the substitution cipher. The key is case-insensitive, so whether any character in the key is uppercase or lowercase does not affect the behavior of the program.

The program first checks if the user provided a single command-line argument. If not, it outputs an error message and returns 1. If the key provided is not exactly 26 characters long, the program outputs an error message and returns 1. If the key provided contains non-alphabetic characters or has repeating characters, the program outputs an error message and returns 1.

If the key is valid, the program prompts the user to enter the plaintext message they wish to encrypt. The program then encrypts the message by replacing each alphabetical character with the corresponding character in the key. The program preserves the case of the characters in the plaintext message, and non-alphabetical characters are preserved in the output. The program then outputs the ciphertext.

Example Usage
```
$ ./substitution VCHPRZGJNTLSKFBDQWAXEUYMOI
plaintext:  hello, world
ciphertext: jrssb, ybwsp
```

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
