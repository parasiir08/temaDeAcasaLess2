"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).

 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""

sir = input("Introdu un sir de caractere: ")
sir2 = sir.lower()

caracter_consola= input("Introdu un caracter specific: ")
caracter_specific= caracter_consola
count = sir2.count(caracter_specific)

print(f"De {count} ori a aparut caracterul indicat")

