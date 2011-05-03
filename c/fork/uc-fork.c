#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>


int main() {

	pid_t pid;

	printf("Once : pid  %d\n", getpid());

	fork();
	fork();
	pid = fork();

	printf("uc fork sonra : pid  %d, ",pid);
	printf("sonraki child : %d \n",pid);
	exit(EXIT_SUCCESS);
}
