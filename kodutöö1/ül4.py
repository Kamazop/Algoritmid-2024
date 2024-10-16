# Binaarne otsingualgoritm
def binaarne_otsing(arr, sihtmärk): # arr - sorditud täisarvude loend, millest otsime sihtmärki ehk täisarvu
  # määrame ära otsitava ala piirid kahe indeksiga; vasak ja parem
    vasak = 0 # loendi esimese elemendi indeks
    parem = len(arr) - 1 # viimase elemendi indeks
    
    while vasak <= parem:
        keskpunkt = vasak + (parem - vasak) // 2 # otsib keskmise indeksi
        if arr[keskpunkt] == sihtmärk: # võrdleb keskmise indeksi väärtust otsitava täisarvuga
            return keskpunkt  # Kui keskmise indeksi väärtus on võrdne sihtmärgiga siis tagastab selle indeksi
        elif arr[keskpunkt] < sihtmärk: # Kui sihtmärk on suurem kui keskpunkti väärtus, siis otsib parempoolselt alalt
            vasak = keskpunkt + 1  # Otsib parempoolsest alamloendist
        else: # Kui sihtmärk on väiksem, siis otsib vasakpoolselt alalt
            parem = keskpunkt - 1  # Otsib vasakpoolsest alamloendist

    return "Täisarvu ei leitud loendist."  # Kui täisarv pole loendis

sorditud_täisarvud = [1, 3, 5, 7, 9, 11, 13]
sihtmärk = 7

tulemus = binaarne_otsing(sorditud_täisarvud, sihtmärk)
print(tulemus)  # Väljundiks on 3 (sest 7 asub indeksil 3)
