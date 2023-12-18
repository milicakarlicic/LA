#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 101

struct Prelaz {
    int novo_stanje;
    char cifra_kolicnik;
};

int main() {
    // automat[stanje][prelaz] = {novo_stanje, ispis}
    struct Prelaz automat[3][10] = {
    {{0, '0'}, {1, '0'}, {2, '0'}, {0, '1'}, {1, '1'}, {2, '1'}, {0, '2'}, {1, '2'}, {2, '2'}, {0, '3'}},
    {{1, '3'}, {2, '3'}, {0, '4'}, {1, '4'}, {2, '4'}, {0, '5'}, {1, '5'}, {2, '5'}, {0, '6'}, {1, '6'}},
    {{2, '6'}, {0, '7'}, {1, '7'}, {2, '7'}, {0, '8'}, {1, '8'}, {2, '8'}, {0, '9'}, {1, '9'}, {2, '9'}}
    };

    char kolicnik[MAX] = "";

    printf("Unesite broj: ");
    char broj[MAX];
    scanf("%s", broj);

    int duzina = strlen(broj);
    int ostatak = 0;
    for(int i = 0; i < duzina; i++) {
        if(!isdigit(broj[i])) {
            fprintf(stderr, "Nije broj!\n");exit(EXIT_FAILURE);
        }

        int prelaz = broj[i] - '0';
        struct Prelaz pom = automat[ostatak][prelaz];
        ostatak = pom.novo_stanje;
        strcat(kolicnik, &pom.cifra_kolicnik);
    }

    printf("Broj %s pri dijeljenju sa 3 daje kolicnik %s i ostatak %d\n", broj, kolicnik[0] == '0' && strlen(kolicnik) > 1 ? kolicnik + 1 : kolicnik, ostatak);

    return 0;
}
