#include <cs50.h>
#include <stdio.h>
#include <stdint.h>

// define BYTE as a uint8_t
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // read binary, write binary
    FILE *src = fopen(argv[1], "rb");
    FILE *dst = fopen(argv[2], "wb");

    //allocate one byte
    BYTE b;

    // fread -> read one or more bytes
    // where to load those bytes in memory -> &b
    // how big it is? -> sizeof(b)
    // how many of those you want to readč -> 1
    // source -> src
    // do it until there's no more -> while != 0
    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst);
    }

    fclose(dst);
    fclose(src);
}
