#!/usr/bin/python3

import sys, os, re

if len(sys.argv) != 2:
    sys.exit('Neispravan broj argumenata komandne linije')

putanja_dir = sys.argv[1]
if not os.path.isdir(putanja_dir):
    sys.exit('Nije direktorijum')

ka_naziv_dir = re.compile(r'm[mvnrli]\d{5}')
ka_naziv_zadatka = re.compile(r'[1-4]\.(cpp|py|java|c)')
# alas, 1.c, 2.java
# (alas, 1) -> c
# (alas, 2) -> java
# za domaci: alas -> [ekst_1_zad, ekst_2_zad, ekst_3_zad, ekst_4_zad]
studenti = {}
for naziv_poddir in os.listdir(putanja_dir):
    rez = ka_naziv_dir.fullmatch(naziv_poddir)
    if rez is None:
        continue

    putanja_poddir = os.path.join(putanja_dir, naziv_poddir)
    if not os.path.isdir(putanja_poddir):
        continue

    for naziv_zadatka in os.listdir(putanja_poddir):
        rez = ka_naziv_zadatka.fullmatch(naziv_zadatka)
        putanja_zadatak = os.path.join(putanja_poddir, naziv_zadatka)
        if rez is None or not os.path.isfile(putanja_zadatak):
            continue

        # naziv_zadatka '1.c' --> split --> ['1', 'c']
        pom = naziv_zadatka.split('.')
        br_zadatka = int(pom[0])
        ekstenzija = pom[1]
        studenti[(naziv_poddir, br_zadatka)] = ekstenzija

svi_studenti = {}
try:
    f = open(os.path.join(putanja_dir, 'indeksi.txt'))
    for linija in f.readlines():
        pom = linija.split(',')
        alas = pom[0]
        ime_prezime = pom[1].strip()
        svi_studenti[alas] = ime_prezime
    f.close()
except:
    sys.exit('Greska pri citanju iz fajla indeksi.txt')

try:
    f = open(os.path.join(putanja_dir, 'ispit.html'), 'w')

    f.write('<html>\n')
    f.write('<body>\n')
    f.write('<table border = 1>\n')
    f.write('<tr>\n')
    f.write('<th>Ime i prezime</th>\n')
    f.write('<th>Alas nalog</th>\n')
    f.write('<th>1. zadatak</th>\n')
    f.write('<th>2. zadatak</th>\n')
    f.write('<th>3. zadatak </th>\n')
    f.write('<th>4. zadatak</th>\n')
    f.write('</tr>\n')

    for student in svi_studenti:
        f.write('<tr>\n')
        f.write('<td>' + svi_studenti[student] + '</td>\n')
        f.write('<td>' + student + '</td>\n')
        for br_zad in range(1, 5):
            if (student, br_zad) in studenti:
                ekstenzija = studenti[(student, br_zad)]
                f.write('<td>' + ekstenzija + '</td>\n')
            else:
                f.write('<td>' + '-' + '</td>\n')
        f.write('</tr>\n')

    f.write('</table>\n')
    f.write('</body>\n')
    f.write('</html>\n')
    f.close()
except:
    sys.exit('Greska pri pisanju u fajl')
