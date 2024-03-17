#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int longlen(long number);

int main(void)
{
    long int number = get_long("Number: ");
    int len = longlen(number);

    char array[len];
    sprintf(array, "%ld", number);

    for (int i = len - 2, sum_mul = 0; i >= 0; i-=2)
    {
        sum_mul += array[i] * 2;
    }

    for (int i = len - 1, sum_nor = 0; i >= 0; i-=2)
    {
        sum_nor += array[i] - 0;
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
