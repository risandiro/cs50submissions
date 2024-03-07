#include <stdio.h>

int main(void)
{
    int score1 = 72;
    int score2 = 73;
    int score3 = 33;

    printf("Average: %f\n", (score1 + score2 + score3) / 3.0 )
}

/*
Easiest way to switch from integer math to floating point math is to have
at least 1 floating number by changing the denominator by adding .0
*/
