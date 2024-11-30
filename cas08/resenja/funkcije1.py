import sys, re

def procitaj_sve_studente(putanja):
    try:
        f = open(putanja)
        linije = f.readlines()
        f.close()
    except IOError:
        sys.exit('Neuspesno citanje')

    studenti = {}
    ka_split = re.compile(r',\s*')
    for linija in linije:
        rez = ka_split.split(linija)
        alas = rez[0]
        ime_prezime = rez[1].strip()
        studenti[alas] = ime_prezime

    return studenti

def kreiraj_html_tabelu(putanja, studenti, svi_studenti):
    try:
        f = open(putanja, 'w')

        f.write('<html>')
        f.write('<table border = 1>')

        f.write('<tr>')
        f.write('<th>Ime i prezime</th>')
        f.write('<th>Alas</th>')
        f.write('<th>1.</th>')
        f.write('<th>2.</th>')
        f.write('<th>3.</th>')
        f.write('<th>4.</th>')
        f.write('</tr>')

        # svi_studenti: alas -> ime i prezime
        # studenti: (alas, 1) -> c
        for alas in svi_studenti:
            f.write('<tr>')
            f.write('<td>' + svi_studenti[alas] + '</td>')
            f.write('<td>' + alas + '</td>')
            for i in range(1, 5):
                kljuc = (alas, i)
                if kljuc in studenti:
                    ekstenzija = studenti[kljuc]
                else:
                    ekstenzija = '-'
                f.write('<td>' + ekstenzija + '</td>')
            f.write('</tr>')

        f.write('</table>')
        f.write('</html>')
    except IOError:
        sys.exit('Neuspesno pisanje')
