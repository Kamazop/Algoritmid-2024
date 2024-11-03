# Bubble sorti simuleerimine
def bubblesort(massiiv):
  for i in range(len(massiiv)):
    for j in range(0, len(massiiv) - i - 1):  # Võrdleb massiivi elemente
      if massiiv[j] > massiiv[j + 1]:  # Kui massiivi esimene element on suurem kui teine element
        massiiv[j], massiiv[j+1] = massiiv[j+1], massiiv[j]	# Võtab esimese ja teise elemendi ning võrdleb kas esimene on teisest suurem. Kui on siis vahetab kohad.
        print(massiiv)

massiiv = [64, 34, 25, 12, 22, 11, 90]		# Ülesandes ette antud massiiv
bubblesort(massiiv)

# [34, 64, 25, 12, 22, 11, 90]
# [34, 25, 64, 12, 22, 11, 90]
# [34, 25, 12, 64, 22, 11, 90]
# [34, 25, 12, 22, 64, 11, 90]
# [34, 25, 12, 22, 11, 64, 90]
# [25, 34, 12, 22, 11, 64, 90]
# [25, 12, 34, 22, 11, 64, 90]
# [25, 12, 22, 34, 11, 64, 90]
# [25, 12, 22, 11, 34, 64, 90]
# [12, 25, 22, 11, 34, 64, 90]
# [12, 22, 25, 11, 34, 64, 90]
# [12, 22, 11, 25, 34, 64, 90]
# [12, 11, 22, 25, 34, 64, 90]
# [11, 12, 22, 25, 34, 64, 90]
