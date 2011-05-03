#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLINE 100
#define BOYUT 3
void chomp(char s[]) {
	s[strlen(s) - 1] = '\0';
}
void mat_yaz(int  a[][BOYUT]) {

	int i,j;
	char s[MAXLINE];
	FILE *yaz;

	printf("> yazilacak dosyanin ismini giriniz : "); getchar();	/* Tampon */
	fgets(s,MAXLINE,stdin); chomp(s);	/* Tampon */
	yaz = fopen(s, "w");
	if ( !yaz){
		printf("HATA : Dosyaya ulasilamadi\n");
		exit(EXIT_FAILURE);
	}
	for (i = 0; i < BOYUT; i++) {
		for (j = 0; j < BOYUT; j++)
			fprintf(yaz, "%d\t", a[i][j]);
		fprintf (yaz, "\n");
	}
	fprintf (yaz,"\n");
	fclose (yaz);
	printf("' %s ' isimli dosyaya matris basariyla yazildi..\n", s);
}
void sor(int a[][BOYUT]) {
	char n;
don:
	puts("> Sonuc yazilsin mi : (e/h)\n");
	scanf("%c", &n);
	if (n == 'e' || n == 'E')
		mat_yaz(a);
	else if (n == 'h' || n == 'H')
		puts("yazilmadi..");
	else {
		puts("HATA: Ne diyorsun anlamiyorum");
		goto don;
	}
}

void mat_oku(int a[][BOYUT]) {

   	int i, j;
   	char s[MAXLINE];
	FILE *oku;

	puts("> okunacak dosyanin ismini giriniz : \n"); getchar();	/* Tampon */
	fgets(s, MAXLINE, stdin); chomp(s);/* Tampon */

	oku = fopen (s, "r");
	if (!oku) {
		printf("HATA : Dosyaya ulasilamadi\n");
		exit(EXIT_FAILURE);
	}
	i = j = 0;
	while ( !feof(oku) && i++ != BOYUT) {
		for(i = 0; i < BOYUT; i++)
			for(j = 0; j < BOYUT; j++)
				fscanf(oku, "%d", &a[i][j]);
	}
	printf("' %s 'isimli dosyadan okunan mantris b dizisine aktarildi..\n", s);
	fclose (oku);
	sor(a);
}
void mat_topla(int a[][BOYUT], int b[][BOYUT], int c[][BOYUT]) {

	int i, j;
	getchar();	/* Tampon */
	for (i = 0; i < BOYUT; i++)
		for (j = 0; j < BOYUT; j++)
		  	c[i][j] = a[i][j] + b[i][j];
	puts("matrisler toplandi..");
	sor(c);
}
void mat_carp(int a[][BOYUT], int b[][BOYUT], int c[][BOYUT]){

	int i, j, k, top;
	getchar();	/* Tampon */
 	for (i = 0; i < BOYUT; i++) {
       	for (j = 0; j < BOYUT; j++) {
			for (top = 0, k = 0; k < BOYUT; k++)
            			 top += a[i][k] * b[k][j];
         	 	c[i][j] = top;
      		 }
		}
	puts("matrisler carpildi..");
	sor(c);
}
void mat_gir(int a[][BOYUT]) {

	int i, j;
	for (i = 0; i < BOYUT; i++)
			for(j = 0; j < BOYUT; j++){
				printf("\n> Matrisin a[%d][%d]. elamanini giriniz : ", i, j);
				scanf("%d", &a[i][j]);
			}
	getchar();/* Tampon */
	puts("'a' matrisi basariyla hafizaya alindi..");
	sor(a);
}
int main() {
	int sayi;
	char n;
	int a[BOYUT][BOYUT], b[BOYUT][BOYUT], c[BOYUT][BOYUT];
git:
	puts(" _____________________________");
	puts("| Matris girmek   icin  1 'e |");
	puts("| Matrisi okumak  icin  2 'e |");
	puts("| Matris toplamak için  3 'e |");
	puts("| Matris carpmak  için  4 'e |");
	puts("------------------------------ : ");
	scanf("%d", &sayi);
	switch (sayi) {
		case 1:
			mat_gir(a);
			break;
		case 2:
			mat_oku(b);
			break;
		case 3:
			mat_topla(a, b, c);
			break;
		case 4:
			mat_carp(a, b, c);
			break;
		default:
			printf("HATA1 : lutfen listedeki bir sayiyi seciniz\n");
			getchar();
			break;
	}
don:
	puts("> Cikis yapilsin mi?..(e/h)");
	scanf("%c", &n);
	if (n == 'e' || n == 'E')
		puts("\ncikis yapildi...");
	else if (n == 'h' || n == 'H')
		goto git;
	else {
		puts ("HATA : Ne diyorsun anlamiyorum");
		getchar();
		goto don;
	}
	exit(EXIT_SUCCESS);
}
