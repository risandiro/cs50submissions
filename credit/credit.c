#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int card;
    do
    {
        card = get_long("Change owed: ");
    }
    while ();

    int sum = calculate_coins(cents);
    printf("%d\n", sum);
}
