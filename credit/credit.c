#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

    // step 1
    int sum_mul = 0;
    for (int i = len - 2, value; i >= 0; i -= 2)
    {
        value = (array[i] - 48) * 2;
        if (value >= 10)
        {
            sum_mul += value / 10;
            sum_mul += value % 10;
        }
        else
        {
            sum_mul += value;
        }
    }

    // step 2
    int sum_nor = 0;
    for (int i = len - 1; i >= 0; i -= 2)
    {
        sum_nor += (array[i] - 48);
    }
    int final = sum_mul + sum_nor;

    // step 3
    if (final % 10 == 0)
    {
        if (len == 15)
        {
            if ((array[0] == '3' && array[1] == '4') || (array[0] == '3' && array[1] == '7'))
                printf("AMEX\n");
        }
        else if (len == 13)
        {
            if (array[0] == '4')
                printf("VISA\n");
        }
        else if (len == 16)
        {
            if (array[0] == '4')
                printf("VISA\n");

            else if (array[0] == '5')
            {
                if
            }
            else
                printf("INVALID\n");
        }
        else
            printf("INVALID\n");
    }
    else
        printf("INVALID\n");
}

int longlen(long num)
{
    int digits = 1;

    if (num < 0)
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
