#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* <program_adi> programini kullanmak icin su adimlari uygulayin
	$ make <program_adi>
	$ ./<program_adi> 2 x 3
	6
	$ ./<program_adi> 2 - 3
	-1
	$ ./<program_adi> 2 + 3
	5
	$ ./<program_adi> 3 / 3
	1
*/
void err_use(char * pname) {
	fprintf(stdout, "kullanim :<%s> <arg1> <-+x/> <arg2>\n", pname);
	exit(EXIT_FAILURE);
}
void err_opt() {
	fprintf(stdout, "<->, <+>, <x>, </> isleclerinden sadece birini seciniz\n");
	exit(EXIT_FAILURE);
}
int hesap(int arg1, int arg2, char *islem) {
	if (strlen(islem) == 1) {
		if      (*islem == '+') return arg1 + arg2;
		else if (*islem == '-') return arg1 - arg2;
		else if (*islem == 'x') return arg1 * arg2;
		else if (*islem == '/') return arg1 / arg2;
	}
	err_opt();
}
int main(int argc, char *argv[]) {
	if (argc != 4)	err_use(argv[0]);
	printf("%d\n", hesap(atof(argv[1]), atof(argv[3]), argv[2]));
	return 0;
}
