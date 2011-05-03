#include <stdio.h>
#include <stdlib.h>

typedef struct Nokta {
	int a;
	int b;
} nokta;

int main() {
	nokta n, *p;
	n.a = 1;
	n.b = 2;
	printf("n_ilk : %d %d\n", n.a, n.b);
	p = &n;
	p->a = 3;
	p->b = 4;
	printf("n_son : %d %d\n", n.a, n.b);
	printf("p : %d %d\n", p->a, p->b);
	exit(EXIT_SUCCESS);
}
