#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentances(string text);

int main(void)
{
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentances = count_sentances(text);

    float L = (letters / words) * 100.00;
    float S = (words / sentances) * 100.00;

    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);

    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int count_letters(string text)
{
    int counter = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            counter++;
        }
    }
    return counter;
}

int count_words(string text)
{
    int counter = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ' && text[i+1] != ' ')
            counter++;
    }
    return counter;
}

int count_sentances(string text)
{
    int counter = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.' && text[i+1] != '.')
            counter++;
        else if (text[i] == '?' && text[i+1] != '?')
            counter++;
        else if (text[i] == '!' && text[i+1] != '!')
            counter++;
    }
    return counter;
}
