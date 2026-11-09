#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 2:
    sys.exit('Pozivanje: ./2.py putanja_do_html')

putanja_do_dat = sys.argv[1]

if putanja_do_dat[-5:].lower() != '.html':
    sys.exit('Nije html!')

with open(putanja_do_dat) as datoteka:
    sadrzaj = datoteka.read()

# mr12127 -> 127/2012
regex = r'<td>\s*([A-Z][a-z]+)\s+([A-Z][a-z]+)\s*</td>\s*'
regex += r'<td>\s*m[rmips](\d{2})(\d{3})\s*</td>\s*'
regex += r'<td>\s*(\d|[1-4]\d|50)\s*</td>\s*'
regex += r'<td>\s*(\d|[1-4]\d|50)\s*</td>\s'

# [(ime prezime, indeks, ukupan broj poena), ...]
studenti = []
poklapanja = re.findall(regex, sadrzaj)
for poklapanje in poklapanja:
    ime_prezime = poklapanje[0] + ' ' + poklapanje[1]
    
    godina_upisa = '20' + poklapanje[2]
    broj_indeksa = int(poklapanje[3])
    indeks = str(broj_indeksa) + '/' + godina_upisa

    ukupni_poeni = int(poklapanje[4]) + int(poklapanje[5])

    studenti.append((ime_prezime, indeks, ukupni_poeni))

studenti.sort(key = lambda student: student[2], reverse = True)
for student in studenti:
    print(student)