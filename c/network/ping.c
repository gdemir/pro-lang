/*
	Bir IP'ye (belirli aralıklarla) ping atıp, durumunu dönen program
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void kullanim(int argc) {
	if (argc != 2) {
		puts("kullanım : <./ping> <IP adress>");
		exit(EXIT_FAILURE);
	}
}

int main(int argc, char *argv[]) {
	kullanim(argc);

	char host[100] = "ping -w 5 ";
	strcat(host, argv[1]);

	for (;;) {
		if (system(host) != 0) {
			fprintf(stdout,"Bir kopma nedeniyle IP'e baglanamadim cıkıyorum");
			exit(EXIT_FAILURE);
		}
	}
	return 0;
}
