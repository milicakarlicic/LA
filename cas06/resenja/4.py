#!/usr/bin/python3

import re

s = input('Unesite string: ')

rezultat = re.findall(r'a+', s)
n = len(rezultat)
for i in range(n):
    print(str(i) + '. poklapanje je: ' + rezultat[i])
