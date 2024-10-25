#include <stdio.h>

int fun (int n){
    static int x = 0;
    if(n>0){
        x++;
        return fun(n-1) + x;
    }
    return 0;
}

int fun2 (int n){
    if(n>0){
        return fun2(n-1) + n;
    }
    return 0;
}

int main(){
    // Static
    int r;
    r = fun(5);
    printf("Static:\n");
    printf("%d\n", r);

    // Non-Static
    r = fun2(5);
    printf("Non-Static:\n");
    printf("%d\n", r);
    return 0;
} 