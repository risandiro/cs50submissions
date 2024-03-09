#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int compute_score(string word);

int POINTS[] = {
    // A == 1; B == 3; C == 3; D == 2; E == 1...
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
        // if the [i] character in 'h'
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 65];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 97];
        }

        // ASCII 'a' is at index 97
        // in order to get it to index 0, we substract by 97
        // from there on, it goes alphabetically until 'z'
        // after that, we pair the number with the index in our array
        // indexes in the array represent the values aplhabetically
        // once we get the value of the letter we add it to a counter

        // we need to check for the case of letters, because uppercased
        // letters use different indexes in the ASCII
        // checking the case also doesn't add any value to any non letters
    }

    return score;
}
