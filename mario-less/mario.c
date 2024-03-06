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




    for (int i = n; i > 0; i--) {
        int counter = 0
        for (int j = n; j > 0; j--) {

            printf("#");
        }
        printf("\n");
    }
}


// n = 4
// j=4, j=3, j=2, j=1
    // i=4, i=3, i=2, i=1

//   #
//  ##
// ###
//####

// print j-1 (3) space + n - (j-1) hash (4 - 3 = 1) + \n
// print j-1 (2) space + n - (j-1) hash (4 - 2 = 2) + \n
// print j-1 (1) space + n - (j-1) hash (4 - 1 = 3) + \n
// print j-1 (0) space + n - (j-1) hash (4 - 0 = 4) + \n
