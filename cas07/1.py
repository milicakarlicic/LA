#!/bin/python3

import re

tekst = '''ovo je neki string
ovo je drugi red ovo. je$dan'''
lista = re.split(r'\s+', tekst)

brojac = 0
ka_rec = re.compile(r'\w+[.!?,]?$')
for p_rec in lista:
    if ka_rec.match(p_rec) is not None:
        brojac += 1

print(f'Brojac je {brojac}')
