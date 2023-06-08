"""Cititi de la utilizator, o lista de nume, separate prin virgula.
Folosind metoda `.split()` transformati textul de la utilizator intr-o lista de nume.
Pentru fiecare nume cititi nota introdusa de utilizator (numar intreg). Adaugati nota in lista `list_of_marks`.
Apoi:
* afișați pentru fiecare nume, nota care îi aparține.
* calculați suma notelor
* calculați media notelor

Completati campurile din ___ si adaugati codul necesar.
Note: Utilizati indiciele numelui pentru a afla nota dupa indice din `list_of_marks`.
"""
list_of_names1 = []
list_of_marks1 = []
names = input("Introdu o lista de nume prin virgula").split(",")
list_of_names1.extend(names)
marks = input("Introdu notele pentru fiecare nume introdus anterior").split(",")
list_of_marks1.extend(marks)

for i in range(len(list_of_names1)):
    name = list_of_names1[i]
    mark = list_of_marks1[i]
    print(f"Nota {mark} aparține lui {name}")
# Codul pentru a afisa notele

marks_sum = 0
for mark in list_of_marks1:
    marks_sum += float(mark)

print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / len(list_of_marks1)}")
