#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(text);
int count_words(text);
int count_sentances(text);

int main(void)
{
    string text = get_string("Text: ");

    int L = count_letters(text);
    int words = count_words(text);
    int S = count_sentances(text);

    int index = 0.0588 * L - 0.296 * S - 15.8;

    if (index >= 16)
    {
        printf("Grade 16+");
    }
    else if (index < 1)
    {
        printf("Before Grade 1");
    }
    else
    {
        printf("Grade %i", index);
    }
}

int count_letters(text)
{

}

int count_words(text)
{

}

int count_sentances(text)
{
    
}
