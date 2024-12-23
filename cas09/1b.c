#include <stdio.h>
#include <stdlib.h>

#define P 0
#define N 1

int main() {
    int stanje = P;
    int zavrsno_stanje = P;

    printf("Unesite rec: ");

    char slovo;
    while((slovo = getchar()) != EOF && slovo != '\n') {
        if(slovo != '0' && slovo != '1') {
            fprintf(stderr, "Nije binarna rec\n");
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
    i kada prolazimo kroz rec slovo po slovo azuriramo tekuce stanje:
    stanje = prelazi[stanje][slovo - '0'];
    */
    if(stanje == zavrsno_stanje)
        printf("Ima paran broj jedinica\n");
    else
        printf("Nema paran broj jedinica\n");

    return 0;
}
