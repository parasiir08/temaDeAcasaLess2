'''
Scrieți un program care solicită utilizatorului să introducă un șir de caractere și verifică dacă acesta este un palindrom
(adică se citește la fel de la stânga la dreapta și de la dreapta la stânga).
'''
cuvint = input("Introdu un cuvint ")
litere_mici= cuvint.lower()

ultim_caracter= litere_mici[-1]
prim_caracter= litere_mici[0]
polindrom = prim_caracter == ultim_caracter
nu_polindrom = not polindrom

print(f"Cuvintul e polindrom {polindrom}")
print(f"Cuvintul nu este polindrom {nu_polindrom}")