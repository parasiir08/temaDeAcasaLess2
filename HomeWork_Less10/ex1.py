'''
Ro:
De la consola se va introduce o bucata de text.
Calculati de cate ori fiecare cuvant a fost folosit.
Afisati informatia.
'''

text = input("Introdu o bucata de text").split()

for i in set(text):
    print(f"{i} a fost folosit de {text.count(i)}")
