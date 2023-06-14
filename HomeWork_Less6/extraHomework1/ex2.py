'''
Scrieți un program care solicită utilizatorului să
introducă trei numere și afișează cel mai mare număr dintre ele.
'''

numere = input("Introduceți 3 numere prin virgulă: ").split(",")
numere1 = []

for numar in numere:
    numere1.append(int(numar))

max_numar = numere1[0]

for i in range(1, len(numere1)):
    if numere1[i] > max_numar:
        max_numar = numere1[i]

print(f"Cel mai mare număr este:{max_numar}")

