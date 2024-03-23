#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *original = "Hello!";

char *new = malloc(strlen(original) + 1);
for (int i = 0, len = strlen(s); i < len + 1; i++)
{
    new[i] = original[i];
}

// len + 1 because you want to copy the \0 value also
