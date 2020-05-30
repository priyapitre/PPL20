//This program prints string "Hello World" after one second using a thread.

#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *hello(void *args) {
	while(1) {
		sleep(1);
		printf("Hello World\n");
	}
}

int main() {
	pthread_t id;
	int err = pthread_create(&id,NULL,hello,NULL);
	err = pthread_join(id,NULL);
	return 0;
}
