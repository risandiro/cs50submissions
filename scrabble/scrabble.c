#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int compute_score(string word);

int POINTS[] = {
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
};

int main(void)
{
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    int score1 = compute_score(player1);
    int score2 = compute_score(player2);

    if (score1 > score2)
    {
        printf("Player 1 wins!");
    }
    else if (score1 < score2)
    {
         printf("Player 2 wins!");

    }
    else
    {
        printf("Tie!");

    }
    printf("\n");

}

int compute_score(string word)
{
    int score = 0;

    // do for as many times as the array is long
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        // if the [i] character in h
        if (isupper(word[i]))
        {
            // h is 8th char in the POINTS array
            // char h can be also interpreted as 104 in ASCII
            // if we convert the first letter to be a we substract by 97
            score += POINTS[word[i] - 65];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 97];
        }
    }

    return score;
}
