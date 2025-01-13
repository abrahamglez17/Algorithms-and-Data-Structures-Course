#include <stdio.h>

int main ()

{
    int A[5]; // [0, 0, 0, 0, 0]
    int B[5] = {1, 2, 3, 4, 5}; // [1, 2, 3, 4, 5]
    int C[10] = {2, 4, 6}; // [2, 4, 6, 0, 0, 0, 0, 0, 0, 0]
    int D[5] = {0}; // [0, 0, 0, 0, 0]
    int E[] = {1, 2, 3, 4, 5}; // [1, 2, 3, 4, 5]

    int i;

    // Print the address of the array elements
    for (i = 0; i < 5; i++)
    {
        printf("A[%d] = %d\n", i, &A[i]);
    }
}