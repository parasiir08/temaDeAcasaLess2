'''
Scrieți un program care solicită utilizatorului să
introducă trei numere și afișează cel mai mare număr dintre ele.
'''

numere = input("Introdu 3 numere prin virgula").split(",")
numere1 = int(numere)
for numar in numere1:
    if numar > [0]:
        print("Primul numar este mai mic")
    elif numar > [1]:
        print("Al 2-lea numar este mai mic")
    elif numar > [2]:
        print("Al 3-lea numar este mai mic")

