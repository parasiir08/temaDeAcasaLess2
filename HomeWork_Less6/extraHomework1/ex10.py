'''
Scrieți un program care solicită utilizatorului să introducă un număr întreg pozitiv
și afișează un model de triunghi utilizând asteriscuri.
De exemplu, dacă utilizatorul introduce 5, programul ar trebui să afișeze:
'''
numar = int(input("Introdu un numar intreg: "))

for i in range(1, numar + 1):
    print('*' * i)
