/*
	kelimeyi ters cevirip ilk 3 hanesini alan program(sadece pointer'la)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAXLINE 100
#define FINAME "ti.txt"
#define FONAME "to.txt"

void reverse(char *s) {
	int c, i, j;
	for (i = 0, j = strlen(s) - 1; j > i; i++, j--)
		c = *(s + i), *(s + i) = *(s + j), *(s + j) = c;
}

char *cut(char *s, int size) {
	int i;
	char *tmp = malloc((strlen(s) + 2) * sizeof(char));

	for (i = 0; i < strlen(s); i++) {
		if (i == size) break; // size'da break'la
		*(tmp + i) = s[i];
	}
	*(tmp + i++) = '\n';
	*(tmp + i) = '\0';
	return tmp;
}

void failure(char *message) {
	fprintf(stderr, "%s", message);
	exit(EXIT_FAILURE);
}

FILE* oku(char *filename) {
	FILE *fp;
	if ((fp = fopen(filename, "r")) == NULL)
		failure("hata : dosya okunamadi");
	return fp;
}
FILE* yaz(char *filename) {
	FILE *fp;
	if ((fp = fopen(filename, "w")) == NULL)
		failure("hata : dosya yazilamadi");
	return fp;
}

int main() {

	FILE *rp = oku(FINAME);

	int i;
	char *s;
	char *words[MAXLINE];

	s = malloc(MAXLINE); // bellek al
	for (i = 0; fscanf(rp, "%s", s) != EOF; i++) {
		reverse(s);
		words[i] = cut(s, 3); // s'in ilk 3 hanesini kes donder .
	}
	free(s); // free'le .
	words[i] = NULL; // words'i kapa .

	FILE *wp = yaz(FONAME);

	for (i = 0; words[i] != NULL; i++) {
		fprintf(wp, "%s", words[i]);
		free(words[i]); // free'le
	}
	exit(EXIT_SUCCESS);
}
