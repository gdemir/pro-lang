#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLINE 300
#define True 1
#define False 0
#define filename "Depo1.txt"

typedef struct ogrenci{
	char *ad;
	char *sd;
	int no;
	char *sfr;
	struct ogrenci *sonra;
}ogr;

/* ilk degerlerimiz	*/
ogr *kayit;
ogr *kafa = NULL;
int liste = False;
int kayit_sayisi = False;

int int_al(char *ileti)
{
	int *N = malloc(sizeof(int));
	printf("%s", ileti);
	scanf("%d", N);
	return *N;
}
char* char_al(char *ileti)
{
	char *s = malloc(sizeof(char));
	printf("%s", ileti);
	scanf("%s", s);
	return s;
}
void imdat(char *ileti)
{
	fprintf(stderr, "%s", ileti); exit(EXIT_FAILURE);
}
int kontrol(int n)
{
	if(!n) puts("===\n[!]  Dikkat liste bos!\n==="); return !n;
}
void yaz(FILE *fp, ogr* yazogr)
{
	fprintf(fp, "%s\t%s\t%d\t%s\n", yazogr->ad, yazogr->sd, yazogr->no, yazogr->sfr);
}
void kayit_cikti(FILE *s)
{
	for (kayit = kafa; kayit; yaz(s, kayit), kayit = kayit->sonra)
		;/*void*/
}
void sonraki(void)
{
	kayit->sonra = kafa;
	kafa = kayit;
	kayit_sayisi++;
	liste = True;
}
void ekle(const char *sifre, int numara, const char *soyad, const char *ad)
{
	kayit = malloc(sizeof(ogr));
	kayit->ad = strdup(ad);
	kayit->sd = strdup(soyad);
	kayit->no = numara;
	kayit->sfr = strdup(sifre);
	sonraki();
}
void kayit_oku(FILE *fp)
{
	char a[MAXLINE], b[MAXLINE], d[MAXLINE];
	int c;
	for ( ; fscanf(fp, "%s%s%d%s", a, b, &c, d) != EOF; ekle(d, c, b, a))
		;/*void*/
}
void kayit_ekle(void)
{
	ekle(char_al("sifresi :"), int_al("no :"), char_al("soyadi :"), char_al("adi :"));
}
void kayit_listele(void)
{
	if (kontrol(liste)) return;
	kayit_cikti(stdout);
}
void* tara(ogr *kayit, int *no)
{
	return (kayit->no == *((int *)no) ) ? (void *)kayit : NULL;
}
void* sorgula( void *(*bak)(ogr *, int *), int *no)
{
	void *sonuc = NULL;
	for (kayit = kafa; kayit; sonuc = (*bak)(kayit, no), kayit = kayit->sonra)
		;/*void*/
	return sonuc;
}
void kayit_bul(void)
{
	if (kontrol(liste)) return;
	int no = int_al("arananin numarasi");
	kayit = sorgula(tara, &no);
	if (kayit)
		yaz(stdout, kayit);
	else
		fprintf(stderr,"kayit bulunamadi");
}
void yukle(void)
{
	FILE *file;
	if ((file = fopen( filename, "r")) == NULL)
		imdat("Dosya okunmak icin acilmadi!");
	kayit_oku(file);
	fclose(file);
}
void bosalt(void)
{
	if (kontrol(liste)) return;
	FILE *file;
	if ((file = fopen(filename, "w")) == NULL)
		imdat("Dosya yazilmak icin acilmadi!");
	kayit_cikti(file);
	fclose(file);
}
int main()
{
	yukle(); // kayitlari dosyadan oku
	bosalt(); // kayitlari dosyaya yaz
	return 0;
}
