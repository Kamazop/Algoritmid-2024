# Liner search algoritm
# Ruumi- ja ajakompleksuse analüüs - Ruumikompleksus sellel algoritmil on O(1), kuna kasutab vaid paari muutujat ning
# ta ei vaja täiendavat mälu kasvava sisendi suuruse jaoks. Ajakompleksus on O(n), sest algoritm peab läbima kogu massiivi, et
# kindlaks teha, kas element on massiivis või mitte.
# Kasutus reaalses maailmas - see algoritm on väikeste andmekogumite puhul efektiivne oma lihtsuse ja ruumikompleksuse poolest.
# Piiranguks on selle algoritmi puhul see, et muutub aeglaseks suuremate massiividega töötamisel, sest iga elemendi läbi käimine võtab rohkem aega.
def linear_search(massiiv, otsitav):  # Defineeritud funktsioon linear_search, argumendiks on "massiiv" ja otsitav element "otsitav"
    for i in range(len(massiiv)): # Käib läbi kõik massiivis olevad elemendid
        if massiiv[i] == otsitav: # Võrdleb kas hetkel valitud element on võrdne otsitava elemendiga
            return i  # Tagastab elemendi indeksi, kui see leitakse
    return -1  # Tagastab -1, kui elementi ei leita

massiiv = [3, 5, 2, 4, 9] # Annan ette suvalise massiivi
otsitav = 4  # Annan ette ka otsitava elemendi
tulem = linear_search(massiiv, otsitav) # Kutsub funktsiooni välja ja tulemuse salvestab muutujasse "tulem"

if tulem != -1: # Kontrollib kas tulem ei ole -1, ehk element on leitud
    print(f"Element {otsitav} leiti indeksilt {tulem}.")
else: # tulem on -1, ehk elementi ei leitud
    print(f"Elementi {otsitav} ei leitud.")
