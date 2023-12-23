%option noyywrap
/* Prilikom pozivanja gcc kompajlera sa opcijama -Wall i -Wextra da ne bismo imali upozorenja */
%option noinput
%option nounput

%{

#include <stdio.h>

/* ovaj dio koda se prenosi u lex.yy.c negdje pri pocetku. Ovdje mozemo ukljucivati zaglavlja koja zelimo da koristimo. Globalne promenljive koje predstavljaju brojace
 */

int brojac_redova = 0;
int brojac_karaktera = 0;

%}

/* u ovom dijelu lex datoteke se stavljaju neke regularne definicije (skracenice za navedene regularne izraze) koje nam koriste da uprostimo regularne izraze koje koristimo u drugom dijelu datoteke
 */

/* sledeci dio, drugi dio, je glavni deo datoteke, i u njemu se definisu regularni izrazi koje prepoznajemo zajedno sa akcijama koje zelimo da se dese kad se pronadje neko pojavljivanje regularnih izraza. U njemu ne smijemo da imamo C-ovske komentare na pocetku linije (mozemo odvojiti nekom bjelinom od pocetka linije i pisati komentar).
 */
%%

\n      { brojac_redova++;  brojac_karaktera++; }
.       { brojac_karaktera++; }

%%

/* treci dio datoteke se prenosi u lex.yy.c na sami kraj i sluzi sa pisanje korisnickog programa. U njemu cemo pisati main funkciju.
 */

int main () {
    yylex();

    printf("Ukupnan broj karaktera je %d, a broj redova je %d.\n", brojac_karaktera, brojac_redova);

    return 0;
}
