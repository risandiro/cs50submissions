#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

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
    char filename[8] = NULL;
    bool new_jpeg = false;

    while(fread(buffer, 1, 512, card) == 512)
    {
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            if (counter != 0)
            {
                FILE *image = fclose()
            }

            sprintf(filename, "%03i.jpg", file_counter);
            FILE *image = fopen(filename, "w");
            FILE *image = fwrite(buffer, 1, 512, image);
        }
        else
        {
             FILE *image = fwrite(buffer, 1, 512, image);
        }
    }
}
