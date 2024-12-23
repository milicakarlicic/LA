%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>

int brojac = 0;

%}

%%

"{"     { brojac++; }

"}"     {
    brojac--;
    if (brojac < 0) {
        return -1;
    }
}

.       { ECHO; /* podrazumevana akcija leksera prilikom nailaska na karakter koji nije opisan regularnim izrazom u okviru dijela za navodjenje pravila - ispis na yyout */}

\n      { ECHO; }

%%

int main () {
    int rez = yylex();

    if (rez == -1) {
        printf(“Zatvorena zagrada koja nije otvorena\n”);
    } else if (brojac == 0) {
        printf("Zagrade su dobro uparene\n");
    } else {
        printf("Otvorene zagrade koja nisu zatvorene\n");
    }

    return 0;
}
