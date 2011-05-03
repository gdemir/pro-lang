#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
/*
   Bu programda;
                 ilk ana process cikar,
                 sonra cocuk process cikar.
                 sleep cocuk processin ana process ile
                 programın bitimine yetismesini saglar
*/
int main() {
	pid_t pid;

	printf("fork once : %d\n", getpid());

	pid = fork();
	sleep(1);

	printf("fork sonra : %d\n", getpid());
	return 0;
}

