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


    int counter = value - 1;
    for (int i = 0; i < value; i++)
    {
        for (int j = 0; j < value; j++)
        {
            do
            {
                printf()
            }
            while (counter < 0);
        }
        counter--;
    }
}




'''
height = 5

print 4x space 1x hash
print 3x space 2x hash
print 2x space 3x hash
print 1x space 4x hash
print 0x space 5x hash
'''
