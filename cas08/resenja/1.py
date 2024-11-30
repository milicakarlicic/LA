#!/bin/python3

import sys, os, re, funkcije1

if len(sys.argv) != 2:
    sys.exit('Pozivanje: ./1.py putanja_do_dir')

putanja_do_dir = sys.argv[1]
if not os.path.isdir(putanja_do_dir):
    sys.exit('Neispravna putanja!')

ka_alas = re.compile(r'm[irslmn]\d{5}')
ka_zadatak = re.compile(r'([1-4])\.(py|java|cpp|c)')

studenti = {}

for alas in os.listdir(putanja_do_dir):
    if ka_alas.fullmatch(alas) is None:
        continue

    putanja_do_alasa = os.path.join(putanja_do_dir, alas)
    if not os.path.isdir(putanja_do_alasa):
        continue

    for zadatak in os.listdir(putanja_do_alasa):
        rez = ka_zadatak.fullmatch(zadatak)
        if rez is None or not os.path.isfile(os.path.join(putanja_do_alasa, zadatak)):
            continue
        # mr22022 -> [(1, c), (3, py)]
        # (mr22022, 1) -> c
        broj_zadatka = int(rez.group(1))
        ekstenzija = rez.group(2)
        studenti[(alas, broj_zadatka)] = ekstenzija

svi_studenti = funkcije1.procitaj_sve_studente(\
os.path.join(putanja_do_dir, 'indeksi.txt'))

funkcije1.kreiraj_html_tabelu(os.path.join(putanja_do_dir, 'ispit.html')\
, studenti, svi_studenti)