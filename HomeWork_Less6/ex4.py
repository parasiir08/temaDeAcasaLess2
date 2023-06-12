"""
Un utilizator va introduce un sir de numere, separate prin virgula de la consola.

Din sirul introdus creaza o lista de numere.

Afla suma elementelor pare si a celor impare din lista si afiseazo.
"""
sir_de_numere = input("Introdu un șir de numere separate prin virgulă: ").split(",")
numere = [int(numar) for numar in sir_de_numere]

suma_pare = 0
suma_impare = 0

for numar in numere:
    if numar % 2 == 0:
        suma_pare += numar
    else:
        suma_impare += numar

print("Suma elementelor pare:", suma_pare)
print("Suma elementelor impare:", suma_impare)
