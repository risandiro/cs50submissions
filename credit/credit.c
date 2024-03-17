#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int longlen(long number);

int main(void)
{
    long int number = get_long("Number: ");
    int len = longlen(number);

    char strnum[len];
    int sum_mul = 0, sum_nor = 0;
    sprintf(strnum, "%li", number);

    for (int i = len - 2; i >= 0; i-=2)
    {
        sum_mul += strnum[i];
    }

    for (int i = len - 1; i >= 0; i-=2)
    {
        sum_nor += strnum[i];
    }

    printf("multiplied: %i", sum_mul);
    printf("\nnormal: %i\n", sum_nor);

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
