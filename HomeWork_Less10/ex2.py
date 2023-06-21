'''
Creaza un program care va inregistra o lista de oaspeti si comenzile lor la un restaurant.

Utilizatorul va introduce la consola cati oaspeti vor fi inregistrati.

Pentru fiecare oaspete, utilizatorul va introduce Numele Oaspetelui si 2 feluri de mancare.

La sfarsit, programul va trebui sa afiseze lista cu oaspeti, ce au comandat, si cat in total va trebui restaurantul sa pregateasca.

Folositi dict
'''

lista_oaspeti = int(input("Introdu numărul de oaspeți care vor fi înregistrați: "))
oaspeti = {}

for i in range(lista_oaspeti):
    nume = input("Introdu numele oaspetelui: ")
    feluri_de_mancare = input("Introdu 2 feluri de mâncare separate prin virgulă: ").split(",")
    oaspeti[nume] = feluri_de_mancare

print("Lista cu oaspeți și comenzile lor:")
total_preparate = 0

for nume, feluri_de_mancare in oaspeti.items():
    print(f"Numele oaspetelui: {nume}")
    print("Felurile de mâncare comandate:")
    for fel in feluri_de_mancare:
        print(f"- {fel}")
        total_preparate += 1

print(f"Numărul total de preparate care trebuie pregătite: {total_preparate}")
