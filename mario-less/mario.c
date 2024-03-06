#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int value;
    do
    {
        value = get_int("Height: ");
    }
    while(value < 1);

    for (int i = 0; i < value; i++)
    {
        for (int j = 0; j < value; j++)
        {
            printf(" ");
        }


    }
}



'''
height = 5

print 4x space 1 x hash
print 3x space 2x hash
print 2x space 3x hash
print 1x space 4x hash



'''
