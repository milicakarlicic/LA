%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>
#include <stdlib.h>

#define KOMENTAR        1
#define LITERAL         2
#define IDENTIFIKATOR   3
#define SEPARATOR       4
#define OPERATOR        5
#define KLJUCNA_REC     6
#define NEPOZNATO       7

%}

%%

var|integer|if|then|end|begin       { return KLJUCNA_REC; }

"{"[^}]*"}"                         { return KOMENTAR; }

[+-]?[0-9]+                         { return LITERAL; }

[+<>-]|:=                           { return OPERATOR; }

[():,;.]                            { return SEPARATOR; }

[a-zA-Z_][a-zA-Z_0-9]*              { return IDENTIFIKATOR; }

[ \t\n]                             { }

.                                   { return NEPOZNATO; }

%%

int main(int argc, char **argv) {
    if(argc == 1 || (yyin = fopen(argv[1], "r")) == NULL) {
                yyin = stdin;
    }

    if(argc == 2 || (yyout = fopen(argv[2], "w")) == NULL) {
                yyout = stdout;
    }

    int token;
    while ((token = yylex()) != 0) {
        switch (token) {
            case KLJUCNA_REC:
                fprintf(yyout, "KR: %s\n", yytext);
                break;
            case IDENTIFIKATOR:
                fprintf(yyout, "ID: %s\n", yytext);
                break;
            case OPERATOR:
                fprintf(yyout, "OP: %s\n", yytext);
                break;
            case SEPARATOR:
                fprintf(yyout, "SEP: %s\n", yytext);
                break;
            case LITERAL:
                fprintf(yyout, "LIT: %s\n", yytext);
                break;
            case KOMENTAR:
                fprintf(yyout, "KOM: %s\n", yytext);
                break;
            case NEPOZNATO:
                fprintf(stderr, "Nepoznata leksema!\n");
                break;
    }

    return 0;
}
