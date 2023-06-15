'''
Scrie un program care generează numere aleatorii între 1 și 10 folosind un buclă while.
 Programul ar trebui să continue generarea de numere până când generează un număr mai mare decât 8.
 Odată ce numărul este mai mare decât 8, programul ar trebui să încheie bucla folosind instrucțiunea break.
'''
import random

x = 0
incercari = 0
while True:
    x = random.randrange(0, 11)
    incercari += 1
    print(x)
    if x > 8:
        print(f"{x} este mai mare ca 8 din a {incercari}-a incercare")
        break
