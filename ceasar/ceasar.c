#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

string cipher_text(string text, int key);


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return printf("Usage: ./caesar key\n");
    }

    for (int i = 0, len = strlen(argv[1]); i < len; i++)
    {
        if (isdigit(i))
        ;
        else
        {
            return printf("Usage: ./caesar key\n");
        }
    }

    int val;
    val = atoi(argv[1]);
    if (val < 0)
    {
        return printf("Usage: ./caesar key\n");
    }

    string user_input = get_string("plaintext:  ");
    string user_output = cipher_text(user_input, val);
    printf("%s", user_output);
}

string cipher_text(string text, int key)
{
    int len = strlen(text);
    string ciphertext = NULL;
    for (int i = 0; i < len; i++)
    {
        if (isalpha(i))
        {
            if(isupper(i))
            {
                int index = i % 26;
                char convert = i - 66 + index;
                ciphertext[i] = convert;
            }
            else
            {
                int index = i % 26;
                char convert = i - 98 + index;
                ciphertext[i] = convert;
            }
        }
        else
        {
            ciphertext[i] = i;
        }
    }
    return ciphertext;
}
