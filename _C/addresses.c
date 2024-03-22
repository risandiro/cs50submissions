#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);

    int *p = &n;
    printf("%p\n", p);

    char *s = "HI!";
    printf("%c", s[0]);
    printf("%c", s[1]);
    printf("%c\n", s[2]);

    printf("%c", *s);
    printf("%c", *(s + 1));
    printf("%c\n", *(s + 2));
}
