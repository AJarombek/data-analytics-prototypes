/**
 * Explain row major matrices in C
 * @author Andrew Jarombek
 * @date 2/15/2020
 */

#include <stdio.h>

int main() {
    printf("C Matrices\n");

    // Unlike Fortran, C matrices are row major.  Remember that is the internal representation and does not
    // impact the code.
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Row 1
    printf("%d\n", matrix[0][0]);
    printf("%d\n", matrix[0][1]);
    printf("%d\n", matrix[0][2]);

    // Row 2
    printf("%d\n", matrix[1][0]);
    printf("%d\n", matrix[1][1]);
    printf("%d\n", matrix[1][2]);

    // Row 3
    printf("%d\n", matrix[2][0]);
    printf("%d\n", matrix[2][1]);
    printf("%d\n", matrix[2][2]);
}