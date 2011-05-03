#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct liste {
	char *ad;
	struct liste *sonra;
}ogr;
ogr *kayit;
ogr *kafa = NULL;

int main() {
	char *ad = "gdemir@dev";
	kayit = malloc(sizeof(ogr));
	kayit->ad = strdup(ad);
	kayit->sonra = kafa;
	kafa = kayit;
	fprintf(stdout, "%s", kayit->ad);
	return 0;
}
