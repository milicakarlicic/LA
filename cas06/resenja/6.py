#!/usr/bin/python3

import re

s = input('Unesite string: ')

rezultat = re.fullmatch(r'\w+', s)
if rezultat == None:
    print('Nije rec')
else:
    print('Jeste rec')
