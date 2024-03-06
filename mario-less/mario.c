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


    for (int j = 0; j < height; j++) {
        for (int i = 0; i < height; i++) {
            if (i + 1 < height) {
                printf(" ");

            } else {
                printf("#");
            }
        }
        printf("\n");
    }
}
