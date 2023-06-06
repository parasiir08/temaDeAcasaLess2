"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""
propozitie=input("Scrie o propozitie").lower()
if "a" in propozitie[:2]:
    print("A este pe a 2-a pozitie")
else:
    print("A nu este pe a 2-a pozitie")