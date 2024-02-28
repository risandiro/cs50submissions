#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c = get_char("Do you agree? "); // double quotes should be used for multiple characters

    if (c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c =='n') // single quotes should be used for a single character
    {
        printf("Not agreed.\n");
    }
}
