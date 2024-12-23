%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>
#include <stdlib.h>

%}

%%

"//".*                              { }

"/*"([^*]|[*][^/])*"*/"             { }


%%

int main () {
    yylex();

    return 0;
}

