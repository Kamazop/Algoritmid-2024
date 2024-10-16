import array as massiiv

x = massiiv.array("j", [])

while True:
  lisa = input("Kas soovid massiivi arvu lisada? yes/no:") # Küsib kasutajalt üle, kas ta soovib arvu lisada
  if lisa.lower() == "yes":
    try:
      lisaint = int(input("Sisesta arv:")) # Kasutaja annab sisendi...
      x.append(lisaint) # see lisatakse massiivi lõppu
      print(f"Massiiv peale lisamist: {x}")
    except ValueError:
      print("Palun sisesta korrektne arv.")
  else:
    print(f"Praegune massiiv: {x}")

kustuta = input("Kas soovid massiivi esimesena lisatud arvu kustutada? yes/no:")
if kustuta.lower == "yes":
  if len(x) > 0:
    print(f"Kustutatud arv: {x.pop(0)}") # Kustutab esimesena lisatud elemendi
    print(f"Massiiv peale kustutamist: {x}")
  else:
    print("Massiiv on tühi, ei saa kustutada")
else:
  print(f"Praegune massiiv: {x}")
