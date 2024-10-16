# FIFO struktuur
import array as massiiv

x = massiiv.array("i", []) # Tekitab tühja massiivi, kuhu hakatakse elemente lisama

while True:
    lisa = input("Kas soovid massiivi arvu lisada? jah/ei: ") # Küsib kasutajalt üle, kas ta soovib arvu lisada
    if lisa.lower() == "jah":
        try:
            lisaint = int(input("Sisesta arv: "))  # Kasutaja annab sisendiks arvu
            x.append(lisaint)  # see lisatakse massiivi lõppu
            print(f"Massiiv peale lisamist: {x}")
        except ValueError:
            print("Palun sisesta korrektne arv.")
    else:
        print(f"Praegune massiiv: {x}")

    kustuta = input("Kas soovid massiivist esimest lisatud arvu kustutada? jah/ei: ") # Küsib kasutajalt, kas soovib esimesena lisatud arvu kustutada
    if kustuta.lower() == "jah":
        if len(x) > 0:
            print(f"Kustutatud arv: {x.pop(0)}")  # Kustutab esimesena lisatud elemendi
            print(f"Massiiv peale kustutamist: {x}")
        else:
            print("Massiiv on tühi, ei saa kustutada.")
    else:
        print(f"Praegune massiiv: {x}")
