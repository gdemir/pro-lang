#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAXLINE 100

typedef struct liste {
	char *yazi;
	struct liste *sonra;
	struct liste *once;
}SATIR;
SATIR *satir;
SATIR *kafa = NULL;
SATIR gecici;

void imdat(char *msj) {
	fprintf(stderr, "%s", msj);
	exit(EXIT_FAILURE);
}
void yaz(FILE *fp, SATIR *satir) {
	fprintf(fp, "%s", satir->yazi);
}
void freele() {
	for(; satir; ) {
		gecici = satir->sonra;
		free(satir);
		satir = gecici;
	}
}
void goruntule() {
	for (satir = kafa; satir; yaz(stdout, satir), satir = satir->once)
		;/*void*/
}
int main() {
	char *depo;
	char c;
	FILE *oku;
	if ( (oku = fopen("depo.txt", "r")) == NULL)
		imdat("dosya okunmak icin acilamadi");

	depo = malloc(sizeof(SATIR));

	for (; fscanf(oku,"%c", &c) != EOF;) {
		if (c != '\n')
			*depo++ = c;
		else {
			*depo = '\0';
			for (; satir; satir=satir->sonra)
				;/*void*/
			satir = malloc(sizeof(SATIR));
			satir->yazi = strdup(depo);
			satir->sonra = kafa;
			satir->once = satir;
			kafa = satir;
			depo = malloc(sizeof(SATIR));
			free(depo);
		}
	}
	goruntule();
	freele();
	return 0;
}
