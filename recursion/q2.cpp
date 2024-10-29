using namespace std;
#include <stdio.h>

void foo(int n, int sum)
{
    int k=0, j=0;

    if(n==0) return;

    k=n%10;
    j=n/10;
    sum=sum+k;
    foo(j, sum);
    printf("k is %d\n", k);
}

int main()
{
    int sum=0;
    foo(2048, sum);
    printf("sum is %d\n", sum);
    return 0;
}