using namespace std;
#include <stdio.h>

// recursive function to find sum of first n natural numbers
int sum(int n) {
    if (n == 0) {
        return 0;
    }
    return n + sum(n - 1);
}

// iterative function to find sum of first n natural numbers
int Isum(int n) {
    int s=0;
    int i;
    for(i=1;i<=n;i++)
        s=s+i;
    return s;    
}

int main() {
    int r;
    int r1;
    r= sum(5);
    printf("%d\n", r);
    r1= Isum(5);
    printf("%d", r1);
    return 0;
}