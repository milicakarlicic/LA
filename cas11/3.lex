%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>

int brojac = 0;

%}

%%

"{"     { brojac++; 
    /* 
     * U slucaju da smo naisli na otvorenu zagradu uvecavamo globalni
     * brojac
     */ 

}

"}"     {
    /* 
     * U slucaju da smo naisli na zatvorenu zagradu smanjujemo globalni
     * brojac pri cemu vodimo racuna da on ne postane negativan jer u tom 
     * slucaju imamo zatvorenu zagradu koja prethodno nije otvorena
     */ 
    brojac--;
    if (brojac < 0) {
        return -1;
    }
}

.       { ECHO; 
    /* 
    * Podrazumevana akcija leksera prilikom nailaska na karakter koji nije opisan 
    * regularnim izrazom u okviru dela za navodjenje pravila - ispis na yyout 
    */
 }

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
