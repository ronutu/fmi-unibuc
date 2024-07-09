#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Utilizare: %s numar\n", argv[0]);
        return 1;
    }

    int numar = atoi(argv[1]);
    int suma = 0;
    while (numar) {
        suma += numar % 10;
        numar /= 10;
    }

    printf("%d\n", suma);
    return 0;
}
