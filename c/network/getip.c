/*
	siteni IP'sini dönen program
*/

#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <arpa/inet.h>

void kullanim(int argc) {
	if (argc != 2) {
		puts("kullanım : <./ping> <host name>");
		exit(EXIT_FAILURE);
	}
}
int main(int argc, char *argv[]) {
	kullanim(argc);
	struct hostent *h;
	h = gethostbyname(argv[1]);
	fprintf(stdout, "Host name  : %s\n", h->h_name);
	fprintf(stdout, "IP Address : %s\n", inet_ntoa(*((struct in_addr *)h->h_addr)));
	return 0;
}
