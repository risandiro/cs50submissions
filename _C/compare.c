#include <stdio.h> //standart input/output -> stdio
#include <cs50.h>

int main(void)
{
    int x = get_int("What's x? ");
    int y = get_int("What's y? ");

    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if(x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    }
}

// C generally tends to "trust" that the user has inputed a correct input and
// therefore it makes C more vulnerable to hacking than other language
