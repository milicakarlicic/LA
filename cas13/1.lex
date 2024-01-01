%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>

#define CJELOBROJNA_KONSTANTA       1
#define REALNA_KONSTANTA            2

%}

DIGIT	    [0-9]
SPACE       [ \t\n]

%%

[+-]?{DIGIT}+                               { return CJELOBROJNA_KONSTANTA; }

[+-]?{DIGIT}+\.{DIGIT}*([Ee][+-]?{DIGIT}+)? { return REALNA_KONSTANTA; }

{SPACE}                                     { }

.                                           { }


%%

int main (int argc, char **argv) {
    if(argc == 1 || (yyin = fopen(argv[1], "r")) == NULL) {
                yyin = stdin;
    }

    if(argc == 2 || (yyout = fopen(argv[2], "w")) == NULL) {
                yyout = stdout;
    }

    int token;

    while (token = yylex()) {
        switch(token) {
            case CJELOBROJNA_KONSTANTA:
                fprintf(yyout,"Pronadjena cjelobrojna konstanta: %s\n", yytext);
                break;
            case REALNA_KONSTANTA:
                fprintf(yyout, "Pronadjena realna konstanta: %s\n", yytext);
                break;
        }
    }

    fclose(yyin);
    fclose(yyout);

    return 0;
}
