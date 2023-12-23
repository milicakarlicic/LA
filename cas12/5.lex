%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>

#define CELOBROJNA_KONSTANTA    1
#define REALNA_KONSTANTA        2

%}

/* regularna definicija cifre i bjeline */
CIFRA       [0-9]
BELINA      [ \t\n]

%%

[+-]?{CIFRA}+                                   { return CELOBROJNA_KONSTANTA; }

[+-]?{CIFRA}+\.{CIFRA}*([Ee][+-]{CIFRA}+)?      { return REALNA_KONSTANTA; }

{BELINA}                                        { }

.                                               { }


%%

int main () {
    int token;

    /* pozivamo funkciju sve dok ima tokena na ulazu. Kada leksicki analizator dodje do EOF, on ce vratiti token koji ima vrijednost 0 */
    while (token = yylex()) {
        switch (token) {
            case CELOBROJNA_KONSTANTA:
                    fprintf(yyout,"Pronadjena celobrojna konstanta: %s\n", yytext);
                    break;
            case REALNA_KONSTANTA:
                fprintf(yyout, "Pronadjena realna konstanta: %s\n", yytext);
                break;
        }
    }

    return 0;
}
