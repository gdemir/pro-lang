#include <stdio.h>
#include <sys/wait.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#define MAXLINE 1024

char *KOMUT[MAXLINE];

int wspace(char c) {
	return c == ' ' || c == '\t' || c == '\n';
}

void err_sys(char *msg) {
	fprintf(stderr, "%s\n", msg);
	exit(EXIT_FAILURE);
}

void split(char l[]) {
	char s[MAXLINE];
	int i, j, k;
	int state = 1;

	for (j = 0, i = 0, k = 0; i < strlen(l); i++) {
		if (! wspace(l[i])) {
			s[j++] = l[i];
			state = 1;
		}
		if ((state == 1 && wspace(l[i])) || l[i + 1] == '\0') {
			s[j] = '\0';
			KOMUT[k++] = strdup(s);
			state = 0;
			j = 0;
		}
	}
}

int main() {
	char buf[MAXLINE];
	int status;
	pid_t pid;
	char prompt[] = "gdemir@hummer:$ ";
	printf("%s", prompt);
	while (fgets(buf, MAXLINE, stdin) != NULL) {
		if (buf[strlen(buf) - 1] == '\n')
			buf[strlen(buf) - 1] = '\0';

		if ((pid = fork()) < 0)
			err_sys("hata : fork edilemedi!");
		else if (pid == 0) {
			split(buf);
			execlp(KOMUT[0], KOMUT[0], KOMUT[1], KOMUT[2], KOMUT[3], (char *)0);
			err_sys("hata : calistirilamadi!");
		}
		if ((pid = waitpid(pid, &status, 0)) < 0)
			err_sys("hata : waitpid calismadi!");
		printf("%s", prompt);
	}
	exit(EXIT_SUCCESS);
}
