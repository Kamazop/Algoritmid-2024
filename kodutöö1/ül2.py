import array as massiiv

x = massiiv.array("j", [])

while True:
  lisa = input("Kas soovid massiivi arvu lisada? yes/no:")
  if lisa.lower() == "yes":
    try:
      lisaint = in(input("Sisesta arv:"))
      x.append(lisaint)
      print("Massiiv peale lisamist: {x}")

else:
  print("Praegune massiiv: {x}")
