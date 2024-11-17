#!/usr/bin/python3

import re

tekst = input('Unesite tekst: ')
reci = re.split('\s+', tekst)

brojac = 0
for rec in reci:
    rezultat = re.fullmatch(r'\w+[,.!?]?', rec)
    if rezultat is not None:
        brojac += 1

print(f'Broj reci je {brojac}')