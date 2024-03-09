#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int compute_score(string word);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if (score1 > score2)
    {
        printf("Player");
    }

}

int compute_score(string word)
{

}
