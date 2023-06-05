"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""

propozitie = input("Scrie o propozitie ")
excluded_character = propozitie.replace(",.?!"," ")
print(f"Propozitie fara caractere {excluded_character}")
