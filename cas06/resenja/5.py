#!/usr/bin/python3

import re

s = input('Unesite string: ')

rezultat = re.finditer(r'a+', s)

for poklapanje in rezultat:
    print(f'Poklopljeno: ' + poklapanje.group() + ', pocetak - ' + str(poklapanje.start()) + ', kraj - ' + str(poklapanje.end()))
