'''
Scrieți un program care primește un număr întreg pozitiv
ca intrare și afișează suma tuturor numerelor de la 1 până la acel număr.
'''

numar = int(input("Introdu un numar intreg: "))
suma_numerelor = 0

for i in range(1, numar + 1):
    suma_numerelor += i

print(f"Suma numerelor de la 1 la {numar} este: {suma_numerelor}")
