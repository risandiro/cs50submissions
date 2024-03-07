#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int score1 = 72;
    int score2 = 73;
    int score3 = 33;

    printf("Average: %f\n", (score1 + score2 + score3) / 3.0 );


    /*
    int scores[3];
    scores[0] = get_int("Score: ");
    scores[1] = get_int("Score: ");
    scores[2] = get_int("Score: ");
    */

    int repetitions = get_int("How many scores? ");
    int scores[repetitions], sum;
    for (int i = 0; i < repetitions; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }

    for (int i = 0; i < reperitions; i++)
    {
        sum = sum + scores[i];
    }

    printf("Average: %f\n", (sum / repetitions);
}
