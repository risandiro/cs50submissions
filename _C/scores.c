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

    int reps = get_int("How many scores? ");
    int scores[reps];
    for (int i = 0; i < reps; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
    }

    int sum = 0;
    for (int i = 0; i < reps; i++)
    {
        sum = sum + scores[i];
    }

    printf("Average: %.2f\n", (float) sum / (float) reps);
}
