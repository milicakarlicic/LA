#!/usr/bin/python3

import sys, re

if len(sys.argv) != 2:
    sys.exit('Nevalidan broj arg komandne linije')

putanja = sys.argv[1]

if not putanja.lower().endswith('.html'):
    sys.exit('Nije html!')

try:
    datoteka = open(putanja)
    sadrzaj = datoteka.read()
    datoteka.close()
except IOError:
    sys.exit('Neuspesno citanje ili otvaranje')

regex = r'<tr[^>]*>\s*<td[^>]*>\s*(\w+)\s+(\w+)\s*</td>\s*'
regex += r'<td[^>]*>\s*(m[mirsln]\d{5})\s*</td>\s*'
regex += r'<td[^>]*>\s*(\d|50|[1-4]\d)\s*</td>\s*'
regex += r'<td[^>]*>\s*(\d|50|[1-4]\d)\s*</td>\s*'

lista = re.findall(regex, sadrzaj)

studenti = {}

for element in lista:
    ime = element[0]
    prezime = element[1]

    alas = element[2]
    broj_indeksa = int(alas[-3:])
    godina_upisa = '20' + alas[2:4]
    indeks = str(broj_indeksa) + '/' + godina_upisa
    
    poeni_prakticni = int(element[3])
    poeni_usmeni = int(element[4])
    ukupni_poeni = poeni_prakticni + poeni_usmeni

    # mapa: indeks -> (ime + prezime, ukupan broj poena)
    studenti[indeks] = (ime + ' ' + prezime, ukupni_poeni)
    
sortirani_kljucevi = sorted(studenti.keys(), key = lambda kljuc_iz_mape : studenti[kljuc_iz_mape][1], reverse = True)

for kljuc in sortirani_kljucevi:
    print(f'{kljuc} {studenti[kljuc][0]} {studenti[kljuc][1]}')
