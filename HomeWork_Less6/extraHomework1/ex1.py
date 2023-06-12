'''
Scrieți un program care solicită utilizatorului să introducă
un șir de caractere și numără numărul de caractere din șir
(excluzând spațiile).
'''

sirul = input("Introdu un sir de caractere").split(" ")
nr_caractere = len(sirul)

print(f"Numarul de caractere este {nr_caractere}")