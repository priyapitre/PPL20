#include<stdio.h>
int factrec(int n){
	if (n==0)
		return 1; 
	else
		return n*(factrec(n-1));
}


int main(){
int result; 
result=factrec(4);
printf("The result is: %d",result);
}
