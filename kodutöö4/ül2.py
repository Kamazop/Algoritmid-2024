def create_index_map(suurus):
    return [False] * suurus

def insert(massiiv, väärtus): # Lisamine
    massiiv[väärtus] = True

def exists(massiiv, väärtus): # Kontroll
    return massiiv[väärtus]

suurus = 10  # võtame väärtuste vahemikuks [0, 9]
index_map = create_index_map(suurus)

insert(index_map, 3) # Lisame väärtused
insert(index_map, 7)

# Kontrollime olemasolu
print(exists(index_map, 3))  # True
print(exists(index_map, 5))  # False

# AJakompleksus - väga efektiivne
#    Lisamine O(1)
#    Kontroll O(1)

# Ruumikompleksus
#    Mälu kasutus O(n), kus n on väärtuste ulatus.
#    Kui väärtuste ulatus on suur ja enamik väärtusi puudub, kulub mälu ebaefektiivselt.

# Kasutusvõimalused reaalses maailmas:
# 1. Andmete olemasolu kiire kontrollimine - Näiteks kui on vaja kindlaks teha, kas üks elemnt eksisteerib kogumis (ID number või failinimi).
# 2. Statistika kogumine - Näiteks täisarvude sageduste arvutamisel saab kasutada massiivi, kus iga indeksi väärtus vastab sagedusele.
# 3. Geomeetria ja graafika - 2D-kaartides või pixel-massiivides, kus iga ruudu väärtus tähistab kindlat omadust.
