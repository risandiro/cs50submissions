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

    // convert long into array of chars
    int k = len - 1;
    char array[len];
    array[len + 1] = '\0';

    while (k >= 0)
    {
        array[k] = number % 10 + 48;
        number /= 10;
        k--;
    }

    // step 1 + step 2
    int sum_mul = 0;
    for (int i = len - 2, value; i >= 0; i-=2)
    {
        value = (array[i] - 48) * 2;
        if (value >= 10)
        {
            sum_mul += value / 10;
            sum value += value % 10;
        }
        else
        {
            sum_mul += value;
        }
    }

    int sum_nor = 0;
    for (int i = len - 1; i >= 0; i-=2)
    {
        sum_nor += (array[i] - 48);
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
