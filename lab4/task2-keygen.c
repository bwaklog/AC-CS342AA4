#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define key_file       "keys.txt"
#define START_TIME     1524013729
#define END_TIME       1524020929
#define KEY_SIZE_BYTES 16

int main() {
    int fd = open(key_file, O_CREAT | O_TRUNC | O_WRONLY, 0644);
    if (fd == -1) {
        return 1;
    }

    unsigned char byte;
    char          buff[4];

    for (int i = START_TIME; i <= END_TIME; i++) {
        srand(i);

        for (int j = 0; j < KEY_SIZE_BYTES; j++) {
            byte    = rand() % 256;
            int len = snprintf(buff, sizeof(buff), "%02x", byte);
            write(fd, buff, len);
        }

        write(fd, "\n", 1);
    }

    close(fd);
    return 0;
}
