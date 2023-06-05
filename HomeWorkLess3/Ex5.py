"""
Verificarea unui palindrom
Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""
cuvint = input("Introdu un cuvint ")
litere_mici= cuvint.lower()

ultim_caracter= litere_mici[-1]
prim_caracter= litere_mici[0]
polindrom = prim_caracter == ultim_caracter
nu_polindrom = not polindrom

print(f"Cuvintul e polindrom {polindrom}")
print(f"Cuvintul nu este polindrom {nu_polindrom}")



