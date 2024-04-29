typedef struct node
{
    int number;
    struct node *next;
} node;

/* if we want to use node in the definition itself, we must
declare it first by putting it's name after typedef struct */

node n* = malloc(sizeof(node));
n -> number = 1;
n -> next = NULL;

/* if you don't declare NULL, it will point to garbage value*/
