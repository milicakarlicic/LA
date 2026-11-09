#!/usr/bin/python3

import funkcije_3

x = int(input('Unesite 1. broj: '))
y = int(input('Unesite 2. broj: '))

print('Zbir je:')
funkcije_3.ispis(funkcije_3.zbir(x, y))

print('Razlika je:')
funkcije_3.ispis(funkcije_3.razlika(x, y))
