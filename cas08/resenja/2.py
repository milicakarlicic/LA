#!/usr/bin/python3

import sys, re, os, shutil

# domaci: Implementirati funkciju za rekurzivni obilazak i filtriranje direktorijuma

if len(sys.argv) != 2:
    sys.exit('Pozivanje: ./2.py putanja_do_dir')

# ../../../dir
putanja_dir = sys.argv[1]
if not os.path.isdir(putanja_dir):
    sys.exit('Neispravna putanja!')

# ../../../backup_dir
indeks_sep = putanja_dir.rfind(os.sep)
naziv_dir = putanja_dir[indeks_sep + 1:]
putanja_backup = putanja_dir[:indeks_sep + 1] + "backup_" + naziv_dir
print(putanja_backup)
backup_dir = shutil.copytree(putanja_dir, putanja_backup, dirs_exist_ok = True)

ka_naziv = re.compile(r'[A-Z0-9]')

for (putanja_do_tekuceg_dir, lista_dir, lista_dat) in os.walk(putanja_backup):
    for direktorijum in lista_dir:
        putanja_element = os.path.join(putanja_do_tekuceg_dir, direktorijum)
        if ka_naziv.match(direktorijum) is None:
            shutil.rmtree(putanja_element)

    for datoteka in lista_dat:
        putanja_element = os.path.join(putanja_do_tekuceg_dir, datoteka)
        if ka_naziv.match(datoteka) is None:
            os.remove(putanja_element)