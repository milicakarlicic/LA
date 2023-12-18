#!/usr/bin/python3

import sys, re, os, shutil

def filtriraj_dir(putanja_dir):
    ka_naziv = re.compile(r'[A-Z0-9]')
    for element in os.listdir(putanja_dir):
        putanja_element = os.path.join(putanja_dir, element)
        if os.path.isfile(putanja_element):
            if ka_naziv.match(element) is None:
                os.remove(putanja_element)
        elif os.path.isdir(putanja_element):
            if ka_naziv.match(element) is None:
                shutil.rmtree(putanja_element)
            else:
                filtriraj_dir(putanja_element)


if len(sys.argv) != 2:
    sys.exit('nije dobro pozivanje')

# ../../../dir
putanja_dir = sys.argv[1]
if not os.path.isdir(putanja_dir):
    sys.exit('nije dir')

# ../../../backup_dir
naziv_dir = os.path.basename(putanja_dir)

indeks_sep = putanja_dir.rfind(os.sep)
putanja_backup = putanja_dir[:indeks_sep + 1] + "backup_" + naziv_dir
backup_dir = shutil.copytree(putanja_dir, putanja_backup, dirs_exist_ok = True)

ka_naziv = re.compile(r'[A-Z0-9]')
for (direktorijum, lista_dir, lista_dat) in os.walk(putanja_backup):
    for direkt in lista_dir:
        putanja_element = os.path.join(direktorijum, direkt)
        if ka_naziv.match(direkt) is None:
            shutil.rmtree(putanja_element)

    for dat in lista_dat:
        putanja_element = os.path.join(direktorijum, dat)
        if ka_naziv.match(dat) is None:
            os.remove(putanja_element)
