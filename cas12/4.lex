%option noyywrap
%option noinput
%option nounput

%{

#include <stdio.h>

%}

%%

[?!.,][^ \t\n]              { fprintf(yyout, "%c %c", yytext[0], yytext[1]); }

[ \t]+                      { fprintf(yyout, " "); }

\n+                         { fprintf(yyout, "\n"); }

%%

int main(int argc, char **argv) {
    if (argc == 1 || (yyin = fopen(argv[1], "r")) == NULL) {
        yyin = stdin;
    }

    if (argc == 2 || (yyout = fopen(argv[2], "w")) == NULL) {
        yyout = stdout;
    }

    yylex();

    fclose(yyin);
    fclose(yyout);

    return 0;
}
