#include <stdio.h>

// Head Recursion
void fun(int n){
    if(n>0){
        printf("%d ", n);
        fun(n-1);
    }
}

// Tail Recursion
void fun2(int n){
    if(n>0){
        fun2(n-1);
        printf("%d ", n);
    }
}

int main(){
    int x = 3;
    printf("Head Recursion: ");
    fun(x);
    printf("\nTail Recursion: ");
    fun2(x);
    return 0;
}