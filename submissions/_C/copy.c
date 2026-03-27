#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char *original = "hello!";

    char *new = malloc(strlen(original) + 1);
    if (new == NULL)
    {
            return 1;
    }

    for (int i = 0, len = strlen(original); i < len + 1; i++)
    {
        new[i] = original[i];
    }

    if (strlen(new) > 0)
    {
        new[0] = toupper(new[0]);
    }

    printf("%s\n", original);
    printf("%s\n", new);
}
