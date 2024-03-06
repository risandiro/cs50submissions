#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while(height < 1);


    int counter;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height; j++)
        {
            if (counter > 0) {
                printf(" ");
            }

            else {
                printf("#");
            }
        }
        printf("\n");
        counter--;
    }
}
