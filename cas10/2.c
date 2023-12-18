#include <stdio.h>
#include <stdlib.h>

#define P 0
#define N 1

int main() {
    int stanje = P;
    int zavrsno_stanje = P;

    printf("Unesite rijec: ");

    char slovo;
    while((slovo = getchar()) != EOF && slovo != '\n') {
        if(slovo != '0' && slovo != '1') {
            fprintf(stderr, "Nije binarna rijec\n");
            exit(EXIT_FAILURE);
        }
        switch(stanje) {
            case P:
                if(slovo == '0')
                    stanje = P;
                else
                    stanje = N;
                break;
            case N:
                if(slovo == '0')
                    stanje = N;
                else
                    stanje = P;
        }
    }

    /* drugi nacin:
    int prelazi[2][2] = {{P, N}, {N, P}};
    i kad prolazimo kroz rijec slovo po slovo azuriramo tekuce stanje:
    stanje = prelazi[stanje][slovo - '0'];
    */
    if(stanje == zavrsno_stanje)
        printf("Ima parno jedinica\n");
    else
        printf("Nema parno jedinica\n");

    return 0;
}
