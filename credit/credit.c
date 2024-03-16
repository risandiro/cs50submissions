#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int longlen(long number);

int main(void)
{
    long number = get_long("Number: ");
    int len = longlen(number);

    if (len != 13 || 15 || 16)
    {
        printf("INVALID");
        return 1;
    }

    for (int i = len - 1; i >= 0; i-=2)
    {
        printf("%i", number[i]);
    }
}

int longlen(long num)
{
    int digits = 1;

    if(num < 0)
    {
        printf("longlen error - negative number");
        return -1;
    }

    while (num > 10)
    {
        num /= 10;
        digits++;
    }

    return digits;
}
