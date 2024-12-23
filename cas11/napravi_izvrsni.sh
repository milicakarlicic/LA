#!/usr/bin/bash

# Koriscenje alata flex i prevodjenje programa mozemo uraditi direktno iz
# terminala ili uz pomoc ove skripte.

# Generisanje lex.yy.c datoteke koja sadrzi implementaciju leksera
# na osnovu ulazne specifikacije zadate nasom .lex datotekom
flex 2.lex

# Prevodjenje generisane C datoteke
gcc -Wall -Wextra lex.yy.c
