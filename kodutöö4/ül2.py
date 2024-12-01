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
