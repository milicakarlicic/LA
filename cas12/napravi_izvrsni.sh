#!/usr/bin/bash

flex 2.lex

gcc -Wall -Wextra lex.yy.c
