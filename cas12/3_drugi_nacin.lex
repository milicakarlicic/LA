%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>
#include <stdlib.h>

#define IDENTIFIKATORI          1
#define KLJUCNA_REC             2
#define KOMENTAR                3
#define STRING                  4
#define DIREKTIVA               5
#define KARAKTER                6

// Neophodna deklaracija
void ispisi(char *tekst);

%}

%%

int|double|char|return          {
    fprintf(yyout, "<B><span style=\"color:blue\">%s</span></B>", yytext);
}

[_a-zA-Z][_a-zA-Z0-9]*          {
    fprintf(yyout, "<span style=\"color:black\">%s</span>", yytext);
}

"//".*|"/*"([^*]|[*][^/])*"*/"  {
    fprintf(yyout, "<span style=\"color:grey\">%s</span>", yytext);
}

["](\\["]|[^"])*["]            {
    fprintf(yyout, "<span style=\"color:green\">%s</span>", yytext);
}

'[^']'|'\\['tn]'                {
    fprintf(yyout, "<span style=\"color:yellow\">%s</span>", yytext);
}

#(.|\\\n)+                      {
    fprintf(yyout, "<span style=\"color:orange\">");
    ispisi(yytext);
    fprintf(yyout, "</span>");
}

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
    if (argc == 1 || (yyin = fopen(argv[1], "r")) == NULL) {
        yyin = stdin;
    }

    if (argc == 2 || (yyout = fopen(argv[2], "w")) == NULL) {
        yyout = stdout;
    }

    /* Direktiva `pre` se koristi kako bismo zadrzali nazubljenost koda. */
    fprintf(yyout, "<pre><html><body>\n");
    yylex();
    fprintf(yyout, "</body></html></pre>\n");

    fclose(yyin);
    fclose(yyout);

    return 0;
}
