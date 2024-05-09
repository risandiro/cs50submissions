#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: /recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    uint8_t buffer[512];
    unsigned int file_counter = 0;

    while(fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff)
            if (buffer[1] == 0xd8)
                if (buffer[2] == 0xff)
                    if ((buffer[3] & 0xf0) == 0xe0)
                        {

                        }

    }
}
