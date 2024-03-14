#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0, len = strlen(argv[1]); i < len; i++)
    {
        if (isdigit(argv[1][i]))
        ;
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key;
    key = atoi(argv[1]);
    if (key < 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");

    for (int j = 0, len = strlen(plaintext); j < len; j++)
    {
        if (islower(plaintext[j]))
        {
            printf("%c", ((plaintext[j] - 97 + (key % 26)) % 26) + 97);
        }
        else if (isupper(plaintext[j]))
        {
            printf("%c", ((plaintext[j] - 65 + (key % 26)) % 26) + 65);
        }
        else
        {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
}
