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
        if (isdigit(argv[1][i]))
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
    printf("ciphertext:  %s", user_output);
}

string cipher_text(string text, int key)
{
    int len = strlen(text);
    string ciphertext = "";
    for (int i = 0; i < len; i++)
    {
        if (isalpha(text[i]))
        {
            if(isupper(text[i]))
            {
                int index = text[i] % 26;
                char convert = text[i] - 66 + index;
                strcat(ciphertext, &text[i]);
            }
            else
            {
                int index = text[i] % 26;
                char convert = text[i] - 98 + index;
                strcat(ciphertext, &text[i]);
            }
        }
        else
        {
            strcat(ciphertext, &text[i]);
        }
    }
    return ciphertext;
}
