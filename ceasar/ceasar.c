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
        if (isdigit(i))
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
}
