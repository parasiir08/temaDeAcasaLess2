'''
Scrieți un program care utilizează o buclă while pentru a genera secvența Fibonacci până la un număr dat de termeni.
Secvența Fibonacci este o serie de numere în care fiecare număr este suma celor două numere precedente.
Secvența începe cu 0 și 1.
'''
numar_termeni = int(input("Introduceți numărul de termeni pentru secvența Fibonacci: "))

termen1 = 0
termen2 = 1
numar_generat = 0
numar_termeni_generati = 0

while numar_termeni_generati < numar_termeni:
    print(termen1, end=" ")

    numar_generat = termen1 + termen2
    termen1 = termen2
    termen2 = numar_generat

    numar_termeni_generati += 1
