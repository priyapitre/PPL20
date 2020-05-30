#include <stdio.h>
void some(int a, int b, int c) {
	char buff[4];
	int *retnew;
	retnew = buff + 20;
	(*retnew) = (*retnew) + 7;
}
int main() {
	int k;
	k = 0;
	some(0,1,2);
	k = 1;
	printf("%d \n",k);
	return 0;
}

