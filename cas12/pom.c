#include <stdio.h>

int main() {
    int a = 4;
    int b = -5;

    double c = +2.5;
    double d = 1.5; // 1.

    // ovo je komentar


    /* i ovo je komentar
     * */

    char c = '\n';
    char c2 = '\'';
    int sum = a + b;
    int difference = a - b;
    double product = c * d;
    double quotient = c / d;

    /* i ovo je komentar
     * */

    //printf("Sum: \"%d\n", sum);
    printf("Difference: %d\n", difference);
    printf("Product: %lf\n", product);
    printf("Quotient: %lf\n", quotient);

    return 0;
}
