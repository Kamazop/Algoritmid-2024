# Insertion sort - kuna antud massiiv on osaliselt juba sorteeritud siis jäävad mõned ümbertõstmised ära.
# Antud juhul insertion sort teeb seda kiiremini, kui täielikult sortimata loendi puhul.
ef insertionsort(massiiv):
    for i in range(1, len(massiiv)):
        temp = massiiv[i]  # Võtab elemendi mällu
        j = i - 1

        # Leiab õige koha praegusele elemendile
        while j >= 0 and temp < massiiv[j]: # Võrdleb kas esimene element on väiksem kui teine element
            massiiv[j + 1] = massiiv[j] # Juhul kui on siis tõstab ümber ja võrdleb kolmandat elementi esimese ja teise elemendiga
            j -= 1

        massiiv[j + 1] = temp
        print(massiiv)  # Kuvab peale igat sammu loendi seisu

massiiv = [12, 11, 13, 5, 6, 7] # Etteantud osaliselt sorteeritud loend
print("Algne massiiv on:", massiiv)
insertionsort(massiiv)
print("Sorditud massiiv on:", massiiv)
