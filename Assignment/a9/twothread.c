//This program prints strings "Hello World" and "Goodbye World" using 2 threads.

#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *goodbye(void *args1) {
	printf("Goodbye World\n");
}

void *hello(void *args2) {
	while(1) {
		sleep(1);
		printf("Hello World\n");
		goodbye(NULL);
	}
}

int main() {
	pthread_t id_hello;
	int err = pthread_create(&id_hello,NULL,hello,NULL);
	err=pthread_join(id_hello,NULL);
	return 0;
}
