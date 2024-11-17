#!/usr/bin/python3

import re

s = input('Unesite string: ')

novi_s = re.sub(r'a+', 'X', s, flags = re.I)
print(novi_s)