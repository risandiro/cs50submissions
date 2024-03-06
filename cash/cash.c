#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);

int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);
}

int quarters = calculate_quarters(cents);

int calculate_quarters(int cents)
{

}
