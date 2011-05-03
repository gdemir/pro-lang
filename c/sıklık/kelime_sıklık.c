#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAXLINE 100
#define FILENAME "tmp.txt"

typedef struct yeni {
	char *kelime;
	struct yeni *sonra;
}WORDS;

WORDS *words;
WORDS *kafa = NULL;
WORDS *Htab[MAXLINE];
int i;

void imdat(char *msj) {
	fprintf(stderr, "%s", msj);
	exit(EXIT_FAILURE);
}

int hash(char s[]) {
	int i, top = 0;
	for (i = 0; s[i] != '\0'; i++)
		top += i * s[i];
	return top % MAXLINE;
}

void yaz(FILE *fp, WORDS *words) {
	fprintf(fp, "%s", words->kelime);
}

void cikti(FILE *fp) {
	for (i = 0; i < MAXLINE; i++)
		if ((words = Htab[i]) != NULL) {
			for (yaz(fp, words); words; words = words->sonra)
				fprintf(stdout, "*");
			puts("");
		}
}

int kelime_sonu(char c) {
	return c == ' ' || c == '\t';
}

int main() {

	FILE *oku;
	if ((oku = fopen(FILENAME, "r")) == NULL)
		imdat("dosya okunmak icin acilmadi");
	char c;
	char depo[MAXLINE];
	for (i = 0; fscanf(oku, "%c", &c) != EOF; ) {
		depo[i++] = c;
		if (kelime_sonu(c)) {
			depo[i] = '\0';
			words = malloc(sizeof(WORDS));
			words->kelime = strdup(depo);
			words->sonra = Htab[hash(depo)];
			Htab[hash(depo)] = words;
			i = 0;
		}
	}
	cikti(stdout);
	return 0;
}
