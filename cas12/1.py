#!/usr/bin/python3

import sys, re

putanja = "automat.txt"

linije = []
try:
    f = open(putanja)
    linije = f.readlines()
    f.close()
except IOError:
    sys.exit('nije dobro citanje')

linije = list(filter(lambda l: not l.startswith("#"), linije))

azbuka = linije[0]
rez = re.fullmatch(r'azbuka:\s*([a-z])\s*-\s*([a-z])\s*', azbuka)
if rez is None:
    sys.exit('datoteka nije dobro zadata')
prvo_slovo = rez.group(1)
drugo_slovo = rez.group(2)
azbuka = []
for i in range(ord(prvo_slovo), ord(drugo_slovo) + 1):
    azbuka.append(chr(i))

stanja = linije[1]
rez = re.fullmatch(r'stanja:\s*(\d+)\s*-\s*(\d+)\s*', stanja)
if rez is None:
    sys.exit('datoteka nije dobro zadata')
prvo_stanje = int(rez.group(1))
drugo_stanje = int(rez.group(2))
stanja = list(range(prvo_stanje, drugo_stanje + 1))

pocetna_stanja = linije[2]
rez = re.fullmatch(r'pocetna:\s*((\d+\s+)+)\s*', pocetna_stanja)
if rez is None:
    sys.exit('datoteka nije dobro zadata')
pocetna_stanja = rez.group(1)[:-1]
pocetna_stanja = re.split(r'\s+', pocetna_stanja)
if len(pocetna_stanja) > 1:
    sys.exit('nije DKA!')
pocetno_stanje = int(pocetna_stanja[0])
if pocetno_stanje not in stanja:
    sys.exit('stanje ne postoji')

zavrsna_stanja = linije[3]
rez = re.fullmatch(r'zavrsna:\s*((\d+\s+)+)\s*', zavrsna_stanja)
if rez is None:
    sys.exit('datoteka nije dobro zadata')
zavrsna_stanja = rez.group(1)[:-1]
zavrsna_stanja = re.split(r'\s+', zavrsna_stanja)
zavrsna_stanja = [int(x) for x in zavrsna_stanja]
for zavrsno in zavrsna_stanja:
    if zavrsno not in stanja:
        sys.exit('stanje ne postoji')

automat = {}
prelazi = linije[4:]
ka = re.compile(r'(\d+)\s+([a-z])\s+(\d+)\s+')
for prelaz in prelazi:
    rez = ka.fullmatch(prelaz)
    if rez is None:
        sys.exit('dat nije dobro zadata')

    prvo_stanje = rez.group(1)
    slovo = rez.group(2)
    drugo_stanje = rez.group(3)

    kljuc = (prvo_stanje, slovo)
    if kljuc in automat:
        sys.exit('nije DKA')
    automat[kljuc] = drugo_stanje

print(automat)
