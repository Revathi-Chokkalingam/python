#include <stdio.h>

int main(void) {
	int i,a ,b;
	scanf("%d %d", &a,&b);
	for (i=a; i<b+1 ;i++)
	    if( i%2==0)
	      printf("%d" "\t",i);
	return 0;
}
