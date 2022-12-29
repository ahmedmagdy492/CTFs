#include <stdio.h>
#include <stdlib.h>

#define LEN 1229

int primes[] = {  };

int main(int argc, char** argv) {
	if(argc == 2) {
		long long n = atoll(argv[1]);
		int a = 0;
		
		for(int i = 0;i < LEN; i++) {
			a = primes[i];
			if(n % a == 0) {
				printf("a -> %d\n", a);
				
			}
			else if(a >= 1000) {
				break;
			}
			else {
				printf("a -> %d is not working\n", a);
			}
		}
	}
	else {
		printf("please provide N\n");
	}
}
