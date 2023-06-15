'''
Scrie un program care primește o listă de numere ca intrare.
Programul ar trebui să calculeze produsul tuturor numerelor din listă.
Cu toate acestea, dacă produsul depășește 100, programul ar trebui să oprească calculul și să afișeze
un mesaj care indică că produsul este prea mare.
Folosește o buclă for și instrucțiunea break pentru a încheia bucla când este necesar.
'''

user = input("Introdu o lista de numere prin virgula ").split(",")
produs = 1

for x in user:
    produs *= int(x)
    if produs > 100:
        print("Produsul este prea mare")
        break
    print(produs)

