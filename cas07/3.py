#!/usr/bin/python3

import sys, re, json

# funkcije za rad sa json formatom:
# dumps - od python reprezentacije dobijamo json reprezentaciju
# loads - od json reprezentacije dobijamo python reprezentaciju
# dump - za upis json/python reprezentacije u datoteku
# load - za citanje json reprezentacije iz datoteke i dobijanje python objekta

if len(sys.argv) != 2:
    sys.exit('Neispravan broj argumenata komandne linije')

putanja = sys.argv[1]
if not putanja.lower().endswith('.json'):
sys.exit('Nije json')

try:
    f = open(putanja, 'r')
    reg_izrazi = json.load(f)
    f.close()
except:
    sys.exit('Neuspesno otvaranje datoteke')

tekst = """Ovo je neki te323kst. Treba provjer321iti koliko puta se nal5453aze
r1312egularni izrazi u njemu."""

brojac = 0
for element in reg_izrazi:
    reg_izraz = element['regex']
    br_pojavljivanja = element['broj_pojavljivanja']
    if len(re.findall(reg_izraz, tekst)) == br_pojavljivanja:
        print(reg_izraz)
        brojac += 1

print(f'Brojac je: {brojac}')
