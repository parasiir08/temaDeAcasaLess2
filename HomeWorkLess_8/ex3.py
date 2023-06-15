'''
Scrie un program care primește o listă de numere ca intrare.
Programul ar trebui să calculeze produsul tuturor numerelor din listă.
Cu toate acestea, dacă produsul depășește 100,
programul ar trebui să oprească calculul și să afișeze un mesaj care indică că produsul este prea mare.
olosește o buclă while și instrucțiunea break pentru a încheia bucla când este necesar.
'''

user = input("Introdu o lista de numere prin virgula ").split(",")
produs = 1
index = 0

while index < len(user):
    numar = int(user[index])
    produs *= numar
    print(produs)
    if produs > 100:
        print("Produsul este prea mare")
        break
    index += 1