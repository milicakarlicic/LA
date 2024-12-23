#!/usr/bin/python3

'''
Sa predavanja:

    Konstrukcija automata:
        - Gluskov
        - Tompson
        - direktno (u slucaju veoma jednostavnih regularnih jezika)

    Determinizacija, upotpunjavanje, minimalizacija

    Proizvod automata

    Za prakticni ispit dolazi u obzir samo implementacija deterministickog KA.

-------------------------------------------------------------------------------------
Direktna konstrukcija automata: 
    - moguca stanja: P (paran broj jedinica), N (neparan broj jedinica)
    - pocetno stanje - P: na pocetku je broj jedinica jednak nuli
    - zavrsno stanje - P: rec prihvatamo ukoliko sadrzi paran broj jedinica
    - ako smo u stanju P i procitamo 1 prelazimo u stanje N, inace ostajemo u stanju P
    - ako smo u stanju N i procitamo 1 prelazimo u stanje P, inace ostajemo u stanju N

Kontruisani automat je potpun i deterministicki.
'''

import re, sys

stanje = 'P'
zavrsno_stanje = 'P'

rec = input('Unesite rec: ')

ka_binarno = re.compile(r'(0|1)+')
rez = ka_binarno.fullmatch(rec)
if rez is None:
    sys.exit('Nije binarna rec')

# P, 0 -> P
# P, 1 -> N
# N, 0 -> N
# N, 1 -> P
prelazi = {('P', 0) : 'P', ('P', 1) : 'N', ('N', 0) : 'N', ('N', 1) : 'P'}

for slovo in rec:
    slovo = int(slovo)
    if (stanje, slovo) in prelazi:
        stanje = prelazi[(stanje, int(slovo))]
    else:
        sys.exit('Ne prihvata')

if stanje == zavrsno_stanje:
    print('Ima paran broj jedinica')
else:
    print('Nema paran broj jedinica')
