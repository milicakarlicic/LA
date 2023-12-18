#!/usr/bin/python3

import re, sys

stanje = 'P'
zavrsno_stanje = 'P'

rijec = input('Unesite rijec: ')

ka_binarno = re.compile(r'(0|1)+')
rez = ka_binarno.fullmatch(rijec)
    if rez is None:
        sys.exit('Nije binarna rijec')

# P, 0 -> P
# P, 1 -> N
# N, 0 -> N
# N, 1 -> P
prelazi = {('P', 0) : 'P', ('P', 1) : 'N', ('N', 0) : 'N', ('N', 1) : 'P'}

for slovo in rijec:
    slovo = int(slovo)
    if (stanje, slovo) in prelazi:
        stanje = prelazi[(stanje, int(slovo))]
    else:
        sys.exit('Ne prihvata')

if stanje == zavrsno_stanje:
    print('Ima parno jedinica')
else:
    print('Nema parno jedinica')
