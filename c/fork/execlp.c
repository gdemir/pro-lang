#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

void imdat(char *msj) {
	fprintf(stderr, "%s", msj);
	exit(EXIT_FAILURE);
}
int main() {

	pid_t pid;

	if ((pid = fork()) < 0)
		imdat("hata : fork edilemedi!");

	if (pid == 0) { // cocuk ?
		execlp("/bin/ls", "ls", "-l", (char *)0);
		imdat("hata : execlp calistirilamadi!");
	}

	if (pid > 0)  //anne ?
		sleep(2); //anne, cocugu 2sn bekle.

	exit(EXIT_SUCCESS);
}
