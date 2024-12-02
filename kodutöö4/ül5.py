class TopeltRäsi:
    def __init__(self, suurus):
        self.suurus = suurus
        self.tabel = [None] * suurus
        self.kasutatud_pesad = 0

    def r1(self, võti):
        return võti % self.suurus

    def r2(self, võti):
        return 1 + (võti % (self.suurus - 1))

    def lisa(self, võti, väärtus):
        if self.kasutatud_pesad == self.suurus:
            raise Exception("Hash tabel on täis")

        indeks = self.r1(võti)
        nihe = self.r2(võti)

        i = 0
        while self.tabel[indeks] is not None and self.tabel[indeks][0] != võti:
            i += 1
            indeks = (indeks + i * nihe) % self.suurus

        if self.tabel[indeks] is None:
            self.kasutatud_pesad += 1
        self.tabel[indeks] = (võti, väärtus)

    def otsi(self, võti):
        indeks = self.r1(võti)
        nihe = self.r2(võti)

        i = 0
        while self.tabel[indeks] is not None:
            if self.tabel[indeks][0] == võti:
                return self.tabel[indeks][1]
            i += 1
            indeks = (indeks + i * nihe) % self.suurus

        return None

    def kuva(self):
        return [(i, self.tabel[i]) for i in range(self.suurus)]

hash_tabel = TopeltRäsi(suurus=7)

elemendid = [(10, "A"), (20, "B"), (30, "C"), (5, "D"), (15, "E"), (25, "F")]
for võti, väärtus in elemendid:
    hash_tabel.lisa(võti, väärtus)

tabeli_sisu = hash_tabel.kuva()
print(tabeli_sisu)

# 1. Eelis ühkordse räsimise ees:
#    - Topelt räsimine vähendab klasterdamist.
#    - Erinevate räsifunktsioonide kasutamisel väheneb korduvate mustrite tõenäosus.
#    - Kui teine räsifunktsioon tagastab väärtuse, mis pole tabeli suurusega ühine, siis käiakse läbi kõik tabeli positsioonid, ehk väldib kokkupõrkeid.

# 2. Aja- ja ruumiline keerukus
#    Parimal juhul - Kui kokkupõrget ei esine, on elemendi leidmis või lisamis aeg O(1)
#    Halvimal juhul - Kui tabel on peaaegu täis ja kokkupõrkeid palju, võib elementidega operatsioonid nõuda kuni O(n), kus n on hash tabeli suurus.

#    Hash tabeli suurus n määrab ruumiline keerukus O(n). Topelträsimisel lisamälu ei kasutata.

# 3. Võimalikud rakendus kohad:
#    1.  Suured andmebaasid
#    2.  Krüptograafia rakendused
