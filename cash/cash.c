#include <cs50.h>
#include <stdio.h>

int calculate_coins(int cents);

int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int sum = calculate_coins(cents);
    printf("%d\n", sum);
}

int calculate_coins(int cents)
{
    int quarters = 0;
    while (cents - 25 >= 0)
    {
        quarters++;
        cents = cents - 25;
    }

    int nickels = 0;
    while (cents - 10 >= 0)
    {
        nickels++;
        cents = cents - 10;
    }

    int pennies = 0;
    while (cents - 5 >= 0)
    {
        pennies++;
        cents = cents - 5;
    }

    int total = quarters + nickels + pennies + cents;
    return total;
}
