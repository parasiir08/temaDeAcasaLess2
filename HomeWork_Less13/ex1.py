'''
Scrie o funcție care primește o listă ca intrare și returnează suma elementelor sale.
Gestionează eroarea de tip TypeError dacă intrarea nu este o listă.
Task:

Definește o funcție care acceptă un singur parametru.
Verifică dacă parametrul este de tip listă folosind o instrucțiune if.
Dacă parametrul este o listă, calculează suma elementelor sale folosind funcția sum() și returnează rezultatul.
Dacă parametrul nu este o listă, generează o eroare de tip TypeError cu un mesaj de eroare adecvat.
'''

def suma_elementelor(lista):
    if not isinstance(lista, list):
        raise TypeError("Parametrul nu este o listă")

    suma = sum(lista)
    return suma

user_input = input("Introdu o listă de numere separate prin spațiu: ").split()
user_input = [int(numar) for numar in user_input]  # Convertim fiecare element în număr întreg

rezultat_suma = suma_elementelor(user_input)
print("Suma elementelor este:", rezultat_suma)




