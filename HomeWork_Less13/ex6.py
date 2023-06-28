import math

def calcul_media_geometrica(lista):
    if 0 in lista:
        raise ZeroDivisionError("Lista conține zero, nu se poate calcula media geometrică")

    produs = 1
    for numar in lista:
        produs *= numar

    media_geometrica = math.pow(produs, 1 / len(lista))
    return media_geometrica

try:
    numere = [float(x) for x in input("Introdu o listă de numere separate prin spațiu: ").split()]
    rezultat = calcul_media_geometrica(numere)
    print("Media geometrică este: {:.2f}".format(rezultat))

except ZeroDivisionError as ex:
    print(ex)
