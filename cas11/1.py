#!/usr/bin/python3

cifre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stanja = [0, 1, 2]

# (stanje, prelaz) → (novo_stanje, ispis)
automat = {}
# stanje 0
automat[(0, 0)] = (0, 0)
automat[(0, 1)] = (1, 0)
automat[(0, 2)] = (2, 0)
automat[(0, 3)] = (0, 1)
automat[(0, 4)] = (1, 1)
automat[(0, 5)] = (2, 1)
automat[(0, 6)] = (0, 2)
automat[(0, 7)] = (1, 2)
automat[(0, 8)] = (2, 2)
automat[(0, 9)] = (0, 3)
# stanje 1
automat[(1, 0)] = (1, 3)
automat[(1, 1)] = (2, 3)
automat[(1, 2)] = (0, 4)
automat[(1, 3)] = (1, 4)
automat[(1, 4)] = (2, 4)
automat[(1, 5)] = (0, 5)
automat[(1, 6)] = (1, 5)
automat[(1, 7)] = (2, 5)
automat[(1, 8)] = (0, 6)
automat[(1, 9)] = (1, 6)
# stanje 2
automat[(2, 0)] = (2, 6)
automat[(2, 1)] = (0, 7)
automat[(2, 2)] = (1, 7)
automat[(2, 3)] = (2, 7)
automat[(2, 4)] = (0, 8)
automat[(2, 5)] = (1, 8)
automat[(2, 6)] = (2, 8)
automat[(2, 7)] = (0, 9)
automat[(2, 8)] = (1, 9)
automat[(2, 9)] = (2, 9)

broj = input('Unesite broj: ')ostatak = 0
kolicnik = 0
for cifra in str(broj):
    prelaz = int(cifra)
    ostatak, cifra_kolicnik = automat[(ostatak, prelaz)]
    kolicnik *= 10
    kolicnik += cifra_kolicnik

print(f'Broj {broj} pri dijeljenju sa 3 daje kolicnik {kolicnik} i ostatak {ostatak}')
