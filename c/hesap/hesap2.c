#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
 Öncelikle <program_adı> programını kullanmak için şu adımları uygulayın
	$ make  <program_adı>
	$ ln -s <program_adı> topla
	$ ln -s <program_adı> cikar
	$ ln -s <program_adı> bol
	$ ln -s <program_adı> carp
	$ ./carp 2 3
	6
	$ ./bol 2 2
	1
	$ ./cikar 1 2
	-1
	$ ./topla 2 1
	3
 */
void err_use(char * pname) {
	fprintf(stdout, "kullanim :<%s> <arg1> <arg2>\n", pname);
	exit(EXIT_FAILURE);
}
void err_opt() {
	fprintf(stdout, "<./topla>, <./cikar>, <./bol>, <./carp> dosyalarından sadece birini seçiniz.\n");
	exit(EXIT_FAILURE);
}
void err_zero() {
	fprintf(stdout, "bölme kuralı gereği, <arg2> değeri 0'dan farklı bir değer olmalıdır.\n");
	exit(EXIT_FAILURE);
}
int hesap(int arg1, int arg2, char *islem) {
	if      (strcmp(islem, "./topla") == 0)	return arg1 + arg2;
	else if (strcmp(islem, "./cikar") == 0) return arg1 - arg2;
	else if (strcmp(islem, "./carp")  == 0)	return arg1 * arg2;
	else if (strcmp(islem, "./bol")   == 0)	{
		if (arg2 != 0)return arg1 / arg2;
		else err_zero();
	}
	else err_opt();
}
int main(int argc, char *argv[]) {
	if (argc != 3)	err_use(argv[0]);
	printf("%d\n", hesap(atof(argv[1]), atof(argv[2]), argv[0]));
	return 0;
}
