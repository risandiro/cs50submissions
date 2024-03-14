#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return printf("Usage: ./caesar key\n");
    }

    for (int i = 0, len = strlen(argv[1]); i < len; i++)
    {
        if (isdigit(argv[1][i]))
        ;
        else
        {
            return printf("Usage: ./caesar key\n");
        }
    }

    int key;
    key = atoi(argv[1]);
    if (key < 0)
    {
        return printf("Usage: ./caesar key\n");
    }

    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");

    for (int j = 0, len = strlen(plaintext); j < len; j++)
    {
        if (isaplha(plaintext[j]))
        {
            printf("%c", plaintext[j]
        }
        else
        {
            printf("%c", (plaintext[j] - 97)
        }
    }
    printf("\n");
}

