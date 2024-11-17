# Binary search
# Ajakompleksuse võrdlus - Kahendotsingul on see O(logn), kus igal sammul jaguneb otsitav ala pooleks, mis ühtlasi teeb otsimise kiiremaks suurte massiividega töötamisel.
# Lineaarotsingul on ajakompleksus O(n), kus halvimal juhul peab läbima kõik elemendid.
# Suurte massiivide puhul on kahendotsing ajaliselt efektiivsem, kui lineaarneotsing. Kuna kahendotsing sorteeritud massiivide puhul vähendab eksponentsiaalselt
# otsitavat piirkonda. Lineearotsingut on võib-olla kasulikum kasutada väikeste ja/või sorteerimata massiivide puhul.
def binary_search(massiiv, otsitav):  # Defineerib funktsiooni binary_search, mis võtab argumendiks sorteeritud massiivi ja otsitava elemendi.
    vasak, parem = 0, len(massiiv) - 1  # Määrab piirid: vasak (0) ja parem (massiivi viimane indeks)
  
    while vasak <= parem:  # Kordab tsüklit, kuni otsingupiirkond pole tühi
        keskmine = (vasak + parem) // 2  # Leiab keskpunkti indeksi täisarvude jagamisel
        if massiiv[keskmine] == otsitav:  # Kontrollib kas keskpunkti väärtus on võrdne otsitava elemendiga
            return keskmine  # Kui väärtus vastab otsitavale, tagastab keskpunkti indeksi
        elif massiiv[keskmine] < otsitav:  # Kui keskpunkti väärtus on väiksem kui otsitav element...
            vasak = keskmine + 1  # liigutab vasakut piiri pärast keskpunkti (sisuliselt välistab väiksemad väärtused)
        else:  # Kui keskpunkti väärtus on suurem kui otsitav element...
            parem = keskmine - 1  # liigutab parema piiri enne keskpunkti (välistab suuremad väärtused)
    return -1  # Kui elementi otsitav ei leita, tagastab -1

massiiv = [1, 2, 3, 4, 5, 8, 9, 11, 13]  # Sorditud täisarvude massiiv
otsitav = 11
tulemus = binary_search(massiiv, otsitav)  # Kutsub välja binary_search funktsiooni ja salvestame tulemuse muutujasse tulemus

if tulemus != -1:  # Kontrollib kas tulemus ei ole -1, ehk element leiti
    print(f"Element {otsitav} leiti indeksilt {tulemus}.")  # Kui element leiti, väljastab sõnumi koos elemendi asukohaga
else:  # Kui tulemus on -1, ehk elementi ei leitud
    print(f"Elementi {otsitav} ei leitud.")  # Väljastab sõnumi, et otsitavat elementi ei leitud
