'''
Scrieți un program care solicită utilizatorului să introducă un număr și afișează toate numerele pare de la 1 la acel număr.
'''
numar = int(input("Introdu un numar: "))
numere_pare = []
for i in range(2, numar + 1, 2):
    numere_pare.append(i)

print(f"Numerele pare până la, {numar}, sunt: {numere_pare}")

