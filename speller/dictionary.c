// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Number of words already counted
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int location = hash(word);
    node *tmp = table[location];
    if (tmp == NULL)
    {
        return false;
    }
    while (tmp != NULL)
    {
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
        tmp = tmp->next;
    }

    return false;
}


// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long total = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        total += tolower(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    char buffer[LENGTH + 1];

    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("cannot open %s\n", dictionary);
        return false;
    }

    while (fscanf(file, "%s", buffer) != EOF)
    {
        unsigned int hash_value = hash(buffer);

        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("couldn't load a note\n");
            return false;
        }

        strcpy(new_node->word, buffer);
        new_node->next = table[hash_value];
        table[hash_value] = new_node;
        word_count++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (word_count > 0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *tmp = table[i];

        while(cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
