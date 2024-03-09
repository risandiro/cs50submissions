#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int compute_score(string word);

int POINTS[] = {
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
}

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

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
}
