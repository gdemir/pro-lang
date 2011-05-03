#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/wait.h>

void child_wait(int pid) {

	printf("CHILD : processim ben .\n");
	printf("CHILD : parent proses proseduru basladi.\n");
	printf("CHILD : pause yaptiran proses id: %d\n", pid);
}

void parent_wait(int child_pid) {

	printf("fork oncesi parent process id : %d\n", getpid());
	printf("PARENT : processim ben .\n");
	printf("PARENT : alt process basladi. alt process id %d\n", child_pid);
	printf("PARENT : alt process 2 saniye sleep modunda\n");
	sleep(2);
	puts("PARENT : alt proses sleep sonrasi uyandi ve isini bitirdi");
}

int main() {

	pid_t pid;

	pid = fork();
	if (pid >= 0) {  // basarili fork?

		if (pid == 0)  // cocuk process
			child_wait(getpid());

		if (pid > 0)   // ana process?
			parent_wait(pid);   // ana process, cocuk process icin beklemede .

	} else {
		puts("hata : fork edilemedi!");
		exit(EXIT_FAILURE);
	}
	exit(EXIT_SUCCESS);
}
