#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define KEY_SIZE_BYTES 16

int main() {

    // srand(time(NULL));

    unsigned char byte;
    for (int i = 0; i < KEY_SIZE_BYTES; i++) {
        byte = rand() % 256;
        printf("%02x", byte);
    }

    printf("\n");

    return 0;
}
