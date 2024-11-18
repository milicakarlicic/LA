#!/usr/bin/python3

import re

s = input('Unesite string: ')

rezultat = re.match(r'[A-Z]{2}', s)
if rezultat != None:
    print('Na pocetku stringa se nalaze 2 velika slova')
else:
    print('Na pocetku stringa se NE nalaze 2 velika slova')
