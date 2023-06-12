'''
Scrieți un program care solicită
utilizatorului să introducă o propoziție și numără numărul de vocale din acea propoziție.
'''

propozitie = input("Scrie o propozitie").lower()

vocale = ["a", "e", "i", "o", "u", "ă", "î", "â"]
suma_vocale = []

for i in propozitie:
    if i in vocale:
        suma_vocale.append(i)
print(f"In propozitie sunt {len(suma_vocale)} vocale")
