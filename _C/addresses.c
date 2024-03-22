#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);

    int *p = &n;
    printf("%p\n", p);

}
