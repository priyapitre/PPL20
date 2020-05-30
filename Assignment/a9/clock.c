//This is a program that implements clock using 3 threads.

#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

int secs,mins,hrs;

void *hours(void *args3) {
	if(mins == 59) {
		mins = -1;
		hrs++;
	}
}

void *minutes(void *args2) {
	pthread_t id_hr;
	if(secs == 59) {
		secs = -1;
		mins++;
	}
	pthread_create(&id_hr,NULL,hours,NULL);
}

void *seconds(void *args1) {
	pthread_t id_min;	
	while(1) {
		sleep(1);
		secs++;
		pthread_create(&id_min,NULL, minutes, NULL);
		printf("%d:%d:%d\n",hrs, mins,secs);
	}
}

int main() {
	pthread_t id_sec;
	int err = pthread_create(&id_sec,NULL,seconds,NULL);
	err = pthread_join(id_sec,NULL);
	return 0;
}
