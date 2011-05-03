#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAXLINE 10000
#define FILENAME "tmp.txt"

static void calkala(char dizi[], size_t n, unsigned int tohum) {
    srand(tohum);
    if (n > 1) {
        size_t i;
        for (i = 0; i < n - 1; i++) {
            size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
            char t = dizi[j];
            dizi[j] = dizi[i];
            dizi[i] = t;
        }
    }
}

void imdat(char *msj) {
	fprintf(stderr, "%s", msj);
	exit(EXIT_FAILURE);
}

