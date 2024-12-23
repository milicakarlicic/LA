%option noyywrap

/*
 * Ove direktive zadajemo flex-u kako ne bismo imali upozorenja prilikom prevodjenja programa
 * sa opcijama -Wall i -Wextra
 */
%option noinput
%option nounput

%{

#include <stdio.h>

/* Ovaj deo koda se prenosi u lex.yy.c negde pri pocetku. Ovde mozemo ukljucivati zaglavlja koja zelimo da koristimo. 
 * Globalne promenljive koje predstavljaju brojace takodje definisemo u ovom delu.
 */

int brojac_redova = 0;
int brojac_karaktera = 0;

%}

/* U ovom delu lex datoteke se mogu pisati regularne definicije (skracenice za navedene regularne izraze) koje nam 
 * koriste da uprostimo regularne izraze koje koristimo u drugom delu datoteke. Primer regularnih definicija bice 
 * prikazan u nekom narednom zadatku.
 */

/* Drugi deo je glavni deo datoteke i u njemu se definisu regularni izrazi koje prepoznajemo zajedno sa akcijama koje zelimo 
 * da se dese kad se pronadje neko pojavljivanje regularnih izraza. Akcije pisemo u programskom jeziku C. 
 * U ovom delu ne smemo imati C-ovske komentare na pocetku linije 
 * (mozemo odvojiti nekom belinom od pocetka linije i pisati komentar).
 */
%%

\n      { brojac_redova++;  brojac_karaktera++; }
.       { brojac_karaktera++; }

%%

/* Treci deo datoteke se prenosi u lex.yy.c na sami kraj i sluzi sa pisanje korisnickog programa. 
 * U ovom delu se pise main funkcija.
 */

int main () {
    yylex();

    printf("Ukupnan broj karaktera je %d, a broj redova je %d.\n", brojac_karaktera, brojac_redova);

    return 0;
}
