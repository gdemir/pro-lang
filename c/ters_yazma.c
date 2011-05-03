#include <stdio.h>

int main(int argc, char *argv[])
{
	if (*argv[1] != '\0') {
		argv[1]++;
		main(argc, argv);
	}
	printf("%c", *argv[1]--);
	return 0;
}
