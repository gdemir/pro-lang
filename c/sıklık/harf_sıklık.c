#include <stdio.h>
#define ASCII_SIZE 128
int bas(int sayi, char harf) {
	return (sayi != 0) ? printf("%c harften: %d\n", harf, sayi) : 0;
}
int main() {
	int s[ASCII_SIZE], c;
	int i = 0;
	for (i = 0; i < ASCII_SIZE; s[i] = 0, i++)
		;/* void */
	s[i] = '\0';
	for (; (c = getchar()) != EOF; s[c]++)
		;/* void */
	for (i = 0; i < ASCII_SIZE; bas(s[i], i), i++)
		;/* void */
	return 0;
}
