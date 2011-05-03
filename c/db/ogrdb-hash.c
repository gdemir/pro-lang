#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define True 1
#define False 0
#define MAXLINE 30
#define filename "db.txt"

typedef struct ogrenci{
	char *ad;
	char *sd;
	char *sfr;
	int no;
	struct ogrenci *sonra;
} ogr;
ogr *n, *gecici;
ogr *hashtab[MAXLINE];

/* ilk degerlerimiz	*/
int liste = False;       /* listede bos = 0 */
int ogrsayisi = False;  /* ogrenci  sayisi = 0 */
int i;

int kontrol(int N) {
	if (!N) fprintf(stderr,"===\n[!]  Dikkat liste bos!\n==="); return !N;
}
void imdat(char* ileti) {
	fprintf(stderr, "%s", ileti); exit(EXIT_FAILURE);
}
int int_al(char* ileti) {
	int *N = malloc(sizeof(int));
	printf("%s", ileti);
	scanf("%d", N);
	return *N;
}
char* char_al(char* ileti) {
	char *s = malloc(sizeof(char));
	printf("%s", ileti);
	scanf("%s", s);
	return s;
}
void yaz(FILE* fp, ogr* yazogr) {
	fprintf(fp, "%s\t%s\t%d\t%s\n", yazogr->ad, yazogr->sd, yazogr->no, yazogr->sfr);
}
unsigned int hash(int no) {
	return no % MAXLINE;
}
ogr* lookup(int no) {
	n = hashtab[hash(no)];
	for ( ; n != NULL; n = n->sonra)
		if (no == n->no)
			return n;
	return NULL;
}
void sonraki(int no) {
	i = hash(no);
 	n->sonra = hashtab[i];
 	hashtab[i] = n;
 	ogrsayisi++;
 	liste = True;
}
void ekle(char* sifre, int no, char* soyad, char* ad) {
 	if (( n = lookup(no)) == NULL) {
 		n = malloc(sizeof(*n));
 		n->no = no;
 		n->ad = strdup(ad);
 		n->sd = strdup(soyad);
 		n->sfr = strdup(sifre);
 		sonraki(no);
 	}else {
		yaz(stdout, n);
		fprintf(stderr, "bu bilgilere sahip kisi kullanmaktadir");
	}
}
void freele(ogr* n) {
	free(n->ad);
	free(n->sd);
	free(n->sfr);
	free(n);
}
void* tara(ogr* n, int* no) {
	return (n->no == *((int *)no) ) ? (void *)n : NULL;
}
void* sorgula(ogr* ilk, void *(*bak)(ogr* , int *), int* no) {
	void *sonuc;
	for (sonuc = NULL, n = ilk; n != NULL; sonuc = (*bak)(n, no), n = n->sonra)
		;/*void*/
	return sonuc;
}

void kayit_free(void) {
	for (i = 0; i < MAXLINE; i++)
		if (hashtab[i] != NULL)
			for (n = hashtab[i], gecici = n->sonra; n != NULL; freele(n), n = gecici)
				;/*void*/
}
void kayit_yaz(FILE *fp) {
	if (kontrol(liste)) return;
	for (i = 0; i < MAXLINE; i++)
		if (hashtab[i] != NULL)
			for (n = hashtab[i]; n != NULL; yaz(fp, n), n = n->sonra)
			;/*void*/
}
void kayit_oku(FILE *fp) {
	char s1[MAXLINE], s2[MAXLINE], s3[MAXLINE];
	int n;
	for (; fscanf(fp, "%s%s%d%s", s1, s2, &n, s3) != EOF; ekle(s3, n, s2, s1))
		;/*void*/
}
void kayit_bul(void) {
	if (kontrol(liste)) return;
	int no = int_al("arananin numarasi");
	n = sorgula(hashtab[hash(no)], tara, &no);
	if (n)
		yaz(stdout, n);
	else
		fprintf(stderr,"kayit bulunamadi");
}
void kayit_ekle(void) {
	ekle(char_al("sifre :"), int_al("no :"), char_al("soyadi :"), char_al("adi :"));
}
void kayit_listele(void) {
	kayit_yaz(stdout);
}
void yukle(void) {
	FILE *file;
	if ((file = fopen( filename, "r")) == NULL
		imdat("Dosya okunmak icin acilmadi");
	kayit_oku(file);
	fclose(file);
}
void bosalt(void) {
	if (kontrol(liste)) return;
	FILE *file;
	if ((file = fopen(filename, "w")) == NULL)
		imdat("Dosya okunmak icin acilmadi!");
	kayit_yaz(file);
	fclose(file);
}
int main() {
	yukle();
	kayit_listele();
	bosalt();
	return 0;
}
