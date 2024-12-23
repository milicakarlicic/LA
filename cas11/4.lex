%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>
#include <stdlib.h>

%}

%%

"//".*                              {
    /* 
     * Prazna akcija u slucaju da smo naisli na jednolinijski komentar. Na taj
     * nacin postizemo brisanje odgovarajucih delova koda
     */
 }

"/*"([^*]|[*][^/])*"*/"             { }


%%

int main () {
    yylex();

    return 0;
}

