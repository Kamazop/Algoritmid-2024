# Rekursiivne Fibonacci funktsioon
# Baasjuhtum 1 - n == 0, siis tagastab 0, kuna esimene Fibonacci arv (F(0)) on 0
# Baasjuhtum 2 - n == 1, siis tagastab 1, kuna teine Fibonacci arv (F(1)) on 1
# Rekursioon - n > 1, siis rakendab rekursiivset lähenemist, ehk iga Fibonacci arv on kahe eelneva Fibonacci arvu summe
# Rekursiivne samm: F(n) = F(n-1) + F(n-2)
# Funktsioon kutsub end rekursiivselt välja seniks kuni jõuab baasjuhtumiteni, siis arvutab järk-järgult jada ülespoole.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 7
print(f"Fibonacci number {n}. positsioonil on: {fibonacci(n)}")
