#include <iostream>
#include <stdlib.h>

using namespace std;

int main()

{
    // 2D array declaration in C++

    // method 1 - created in stack
    int A[3][4] = {{1,2,3,4}, {2,4,6,8}, {3,5,7,9}}; // created in stack

    // method 2 - created in heap
    int *B[3]; // created in stack

    // created in heap
    B[0] = new int[4];
    B[1] = new int[4];
    B[2] = new int[4];

    // method 3 - created in heap

    int **C; // created in stack

    C = new int *[3]; // created in heap

    // created in heap
    C[0] = new int[4];
    C[1] = new int[4];
    C[2] = new int[4];

    // accessing elements of 2D array

    // method 1
    printf("Method 1\n");
    for(int i = 0; i < 3; i++) // rows
    {
        for(int j = 0; j < 4; j++) // columns
        {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }

    // method 2
    printf("Method 2\n");
    for(int i = 0; i < 3; i++) // rows
    {
        for(int j = 0; j < 4; j++) // columns
        {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }

    // method 3
    printf("Method 3\n");
    for(int i = 0; i < 3; i++) // rows
    {
        for(int j = 0; j < 4; j++) // columns
        {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    // 2D array declaration in C

    // method 1 - created in stack

    int D[3][4] = {{1,2,3,4}, {2,4,6,8}, {3,5,7,9}}; // created in stack

    // method 2 - created in heap

    int *E[3]; // created in stack

    // created in heap
    E[0] = (int *)malloc(4 * sizeof(int));
    E[1] = (int *)malloc(4 * sizeof(int));
    E[2] = (int *)malloc(4 * sizeof(int));

    // method 3 - created in heap

    int **F; // created in stack

    F = (int **)malloc(3 * sizeof(int *)); // created in heap

    // created in heap

    F[0] = (int *)malloc(4 * sizeof(int));
    F[1] = (int *)malloc(4 * sizeof(int));
    F[2] = (int *)malloc(4 * sizeof(int));

    // accessing elements of 2D array

    // method 1
    printf("Method 1\n");
    for(int i = 0; i < 3; i++) // rows
    {
        for(int j = 0; j < 4; j++) // columns
        {
            printf("%d ", D[i][j]);
        }
        printf("\n");
    }

    // method 2
    printf("Method 2\n");
    for(int i = 0; i < 3; i++) // rows
    {
        for(int j = 0; j < 4; j++) // columns
        {
            printf("%d ", E[i][j]);
        }
        printf("\n");
    }

    // method 3
    printf("Method 3\n");
    for(int i = 0; i < 3; i++) // rows
    {
        for(int j = 0; j < 4; j++) // columns
        {
            printf("%d ", F[i][j]);
        }
        printf("\n");
    }

    return 0;
}