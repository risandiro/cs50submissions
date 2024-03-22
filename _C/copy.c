#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *original = "Hello!";

char *new = malloc(strlen(s) + 1);
for (int i = 0, len = strlen(s); i < len; i++)
{
    new[i] = original[i];
}
