#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while(n < 1);


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if ((j + i) < n-1) {
                printf(" ");
            }
            else {
                printf("#");
            }

        }
        printf("\n");
    }
}

/*
// n = 4
// j=1, j=2, j=3, j=4
// i=1, i=2, i=3, i=4

---#
--##
-###
####

(j + i) <= n - 1
*/
