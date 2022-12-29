#include <stdio.h>
#include <stdlib.h>

long long gcd(long long a, long long b) {
	if(a == 0)
		return b;
	if(b == 0)
		return a;

	return gcd(b, a%b);
}

int main(int argc, char** argv) {
	if(argc == 3) {
		long long a = atoll(argv[1]);
		long long b = atoll(argv[2]);

		long long result = gcd(a, b);
		printf("%ld\n", result);
	}
	else {
		printf("Invalid a and b\n");
	}
}
