"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""

propozitie = input("Scrie o propozitie ")
excluded_characters = ",.?!"
for char in excluded_characters:
    propozitie = propozitie.replace(char, "")
print(f"Propozitie fara caractere {propozitie}")
