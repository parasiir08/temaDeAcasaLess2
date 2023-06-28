try:
    primul_numar = float(input("Introdu primul număr: "))
    al_doilea_numar = float(input("Introdu al doilea număr: "))

    if al_doilea_numar == 0:
        raise ZeroDivisionError("Al doilea număr nu poate fi zero")

    rezultat = primul_numar / al_doilea_numar
    print("Rezultatul împărțirii este:", rezultat)

except ValueError:
    print("Ai introdus o valoare nevalidă. Introdu numere reale.")
except ZeroDivisionError as ex:
    print(ex)
