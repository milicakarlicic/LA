%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>
#include <stdlib.h>

#define KOMENTAR        1
#define STRING          2
#define IDENTIFIKATOR   3
#define KARAKTER        4
#define DIREKTIVA       5
#define KLJUCNA_REC     6

%}

%%

int|double|"return"|"else if"|char   { return KLJUCNA_REC; }

"//".*|"/*"([^*]|[*][^/])*"*/"       { return KOMENTAR; }

["](\\["]|[^"])*["]                  { return STRING; }

[a-zA-Z_][a-zA-Z_0-9]*               { return IDENTIFIKATOR; }

'.'|'\\[nt']'                        { return KARAKTER; }

#(.|\\\n)+                           { return DIREKTIVA; }

%%

void ispisi(char *tekst) {
    for (int i = 0; tekst[i] != '\0'; i++) {
        if (tekst[i] == '<') {
            fprintf(yyout, "&lt");
        } else if (tekst[i] == '>') {
            fprintf(yyout, "&gt");
        } else {
            fprintf(yyout, "%c", tekst[i]);
        }
    }
}

int main(int argc, char **argv) {
    if(argc == 1 || (yyin = fopen(argv[1], "r")) == NULL) {
                yyin = stdin;
    }

    if(argc == 2 || (yyout = fopen(argv[2], "w")) == NULL) {
                yyout = stdout;
    }

    int token;
    fprintf(yyout, "<pre><html><body>");
    while ((token = yylex()) != 0) {
        switch (token) {
            case KLJUCNA_REC:
                fprintf(yyout, "<B><span style=\"color:blue\">%s</span></B>", yytext);
                break;
            case IDENTIFIKATOR:
                fprintf(yyout, "<span style=\"color:black\">%s</span>", yytext);
                break;
            case STRING:
                fprintf(yyout, "<span style=\"color:green\">%s</span>", yytext);
                break;
            case KOMENTAR:
                fprintf(yyout, "<span style=\"color:grey\">%s</span>", yytext);
                break;
            case KARAKTER:
                fprintf(yyout, "<span style=\"color:purple\">%s</span>", yytext);
                break;
            case DIREKTIVA:
                fprintf(yyout, "<span style=\"color:orange\">");
                ispisi(yytext);
                fprintf(yyout, "</span>");
                break;
        }
    }
    fprintf(yyout, "</body></html></pre>");

    return 0;
}
