#!/usr/bin/python3

import re

s = input('Unesite string: ')

rezultat = re.match(r'pocetak', s, re.I)
if rezultat is not None:
    print('Nalazi se')
else:
    print('Ne nalazi se')