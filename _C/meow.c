#include <stdio.h>

int main(void)
{
    int i = 0;
    while (i < 3)
    {
        printf("meow\n");
        i++;
    }

    printf("-----\n");

    // if you have only one line of code in a loop, you can skip {}
    for(int in = 0; in < 3; in++)
        printf("meow\n");
}
