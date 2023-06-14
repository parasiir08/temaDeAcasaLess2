'''
Scrieți un program care solicită utilizatorului să introducă un șir de caractere și verifică dacă acesta este un palindrom
(adică se citește la fel de la stânga la dreapta și de la dreapta la stânga).
'''
cuvant = input("Introdu un cuvânt: ")
litere_mici = cuvant.lower()

polindrom = True
for i in range(len(litere_mici) // 2):
    if litere_mici[i] != litere_mici[-i - 1]:
        polindrom = False
        break

nu_polindrom = not polindrom

print(f"Cuvântul este palindrom: {polindrom}")
print(f"Cuvântul nu este palindrom: {nu_polindrom}")
