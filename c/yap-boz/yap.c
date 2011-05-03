#include "ulti.h"

int main() {
	FILE *yaz;
	int i, sifre;
	char s[MAXLINE];
	char base[] = { 32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,
			66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,
			100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,
			126,'\0'};

	if ((yaz = fopen (FILENAME, "w")) == NULL)
		imdat("HATA : Dosyaya erisilemedi!");

	puts("\ncevrilcek metini girin : ");  // Not: fgets enter'e basıldıgında çalişan bir fonksiyon oldugundan
	fgets(s, MAXLINE, stdin); 	     // NULL'dan önceki karakter '\n' olarak kaydetmekte
	s[strlen(s) - 1] = '\0'; // <-- dosya yazım sonrası okumada sorun olabileceğinden sorunu aşmak için şu kullanılabilir

	puts("sifreyi giriniz : ");
	scanf("%d", &sifre);

	calkala(base, strlen(base), sifre);

	for (i = 0; s[i] != '\0'; i++)
		s[i] = base[s[i] - ' ']; // s[i] - ' '   =>  chr - 48

	fprintf(yaz, "%s", s);
	fclose(yaz);
	exit(EXIT_SUCCESS);
}
