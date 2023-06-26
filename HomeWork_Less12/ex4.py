'''
Scrieți o funcție Python numită is_prime care verifică dacă un număr dat este prim sau nu.
Funcția ar trebui să primească un singur argument: number (integer) care reprezintă numărul de verificat.
Funcția ar trebui să returneze o valoare booleană care indică dacă numărul este prim.

Sugestie: Un număr prim este un număr mai mare decât 1 și care nu are divizori în afară de 1 și el însuși.

Scrieți un program care utilizează funcția is_prime pentru a face următoarele:

Solicitați utilizatorului să introducă un număr.
Apelați funcția is_prime cu valoarea introdusă.
Afișați dacă numărul este prim sau nu.
'''
def is_prime(number: int):
    for n in range(2, number):
        if number % n == 0:
            print("Acesta nu este un numar prim")
            break
    else:
        print(f"{number} este prim")

number1 = int(input("Introdu un numar sa verificam daca este prim "))
print(is_prime(number1))
