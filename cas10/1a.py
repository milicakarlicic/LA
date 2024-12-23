#!/usr/bin/python3

'''

Transduktor - kao i automat cita rec sa ulaza slovo po slovo i prihvata je u zavisnosti
od ispunjenosti odredjenog uslova. Pored citanja sa ulaza, transduktor moze da pise na 
odgovarajuci izlaz. 
Jedan primer upotrebe transduktora je racunanje kolicnika i ostatka pri deljenju brojeva. 
Kolicnik ispisujemo na standardni izlaz dok ostatak predstavlja stanje u kome smo zavrsili 
sa obradom ulaza.

Konstrukcija transduktora:
    - stanja: moguci ostaci (u slucaju broja 3 to su 0, 1 i 2)
    - pocetno stanje: 0 
    - zavrsno stanje: ostatak koji zelimo da dobijemo (u slucaju deljivosti to je 0)
    - prelazi: ako smo u stanju X i na ulazu se nadje slovo Y onda delimo broj XY sa 3,
    ostatak pri tom deljenju predstavlja novo stanje u koje prelazimo a na izlaz pisemo 
    izracunati kolicnik

 715 : 3 = 2
-6   
-----
 1 --> na izlaz pisemo 2 (tekuci kolicnik) i prelazimo u stanje 1 (zapis na grani za prelaz - 1/2)
 115 --> nastavljamo postupak deljenja


Mozemo deliti brojeve i u drugim brojevnim sistemima koristeci ista pravila pri cemu 
ostaci tj. stanja transduktora mogu ostati u dekadnom formatu. Tada vrednost broja 
racunamo na sledeci nacin:
    - binarni: 30 (u stanju smo 3 a na ulazu se nalazi broj 0)
        30 = 3 * 2^1 + 0 * 2^0 = 6
    - slicno za oktalni i heksadekadni brojevni sistem

'''

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

broj = input('Unesite broj: ')
ostatak = 0
kolicnik = 0
for cifra in str(broj):
    prelaz = int(cifra)
    ostatak, cifra_kolicnik = automat[(ostatak, prelaz)]
    kolicnik *= 10
    kolicnik += cifra_kolicnik

print(f'Broj {broj} pri deljenju sa 3 daje kolicnik {kolicnik} i ostatak {ostatak}')
