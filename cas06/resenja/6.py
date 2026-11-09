#!/usr/bin/python3

import re

s = input('Unesite string: ')

rezultat = re.search(r'[A-Z]{2}', s)
if rezultat != None:
    print('U stringu se nalaze 2 velika slova')
    print('Nadjena slova su: ' + rezultat.group())
else:
    print('U stringu se NE nalaze 2 velika slova')
