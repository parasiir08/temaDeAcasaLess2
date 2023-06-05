"""Declaraţi o variabilă price, de tip int, care va reţine preţul unui produs citit de la tastatură.

* Calculaţi cât va reprezenta 30% din preţul iniţial şi salvaţi valoarea în variabila reducere
*	Scădeţi din preţul iniţial valoarea reducerii, calculate la pasul precedent. Salvaţi valoarea în variabila preţ_final
* Creaţi o variabilă nouă pret_100_lei, şi salvaţi în această variabilă cât va fi preţul iniţial minus 100 lei
* Afişaţi la final ambele preturi.

"""
price = int(input("Introdu pretul "))
reducere1= (30/100) * price
reducere=reducere1
pret_semifinal=price-reducere
pret_final=pret_semifinal
pret_100_lei=price-100

print(f"Pretul final este {pret_final}, iar pretul -100 lei este {pret_100_lei}")
