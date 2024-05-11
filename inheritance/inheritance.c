// Simulate genetic inheritance of blood type

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
} person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    person *p = malloc(sizeof(person));

    if (generations > 1)
    {
        // for each parent create another 2 parents recursively until we get to last generation
        // each parent[0] and parent[1] is storing a pointer to another person struct and so on..
        p->parents[0] = create_family(generations - 1);
        p->parents[1] = create_family(generations - 1);

        // childs -> parent[0] and his parent[0] (childs grandfather) -> alleles
        // since the grandfather is our last generation (generation 3), we start from there
        p->alleles[0] = p->parent[0]->alleles[rand() % 2];
        p->alleles[1] = p->parent[1]->alleles[rand() % 2];
        // alleles array of 2 characters, there's alleles 0 and alleles 1
        // we want to choose at random which one of them the child is going to inherit
        // % 2 makes it to divide between odd and even so it's 50/50
    }
    else
    {
        // if we get to the  last generation after our recursive function comes to generations = 1
        // we set it's parents to NULL, because that data will be unknown for us.
        p->parents[0] = NULL;
        p->parents[1] = NULL;

        p->alleles[0] = random_allele();
        p->alleles[1] = random_allele();
        // since we start our count from here, we must give them 2 random alleles
    }

    //return the pointer to newly created tree of people
    return p;
}

// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    if (p == NULL)
    {
        return;
    }

    // TODO: Free parents recursively

    // TODO: Free child
}

// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }

    // Print parents of current generation
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Randomly chooses a blood type allele.
char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
