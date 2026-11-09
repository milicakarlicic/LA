#!/usr/bin/python3

# Numeracija argumenata komandne linije:
#    ./naziv.py arg1 arg2 ag3 …
#          0          1      2      3   …
# Uključivanje sys modula u kome se nalaze argumenti komandne linije. U nastavku
# svim funkcijama i promenljivim iz modula sys pristupamo sa sys.naziv_funkcije ili 
# sys.naziv_promenljive. 
# Moguće je korišćenje funkcija i promenljivih iz nekog modula bez prefiksa naziva tog
# modula: from naziv_modula import *
import sys
 
if len(sys.argv) != 2:
    sys.exit('Pozivanje: ./naziv.py putanja_do_fajla')

# Prvi način:  
# try:
#     f = open(sys.argv[1], 'r')
#     sadrzaj = f.read()
#     f.close()
# except:
#     sys.exit('Greska pri otvaranju fajla')

# Drugi način:
with open(sys.argv[1], 'r') as f:
    sadrzaj = f.read()

# Za čitanje iz datoteke: f.read(), f.readline(), f.readlines()...
# Za pisanje u datoteku: f.write(...)

print(sadrzaj)