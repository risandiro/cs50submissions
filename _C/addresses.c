#include <stdio.h>

int adresses(void)
{
    int n = 50;
    printf("%p\n", &n);

    int *p = &n;
    printf("%p\n", p);

}

int main(void)
{
    char *s = "HI!";
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    printf("%c\n", s[3]);
}
