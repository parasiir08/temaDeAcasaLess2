"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""

parola = input("Introdu o parola ")
lungime_parola= len(parola)
if lungime_parola>=8 and (not parola.islower() and not parola.isupper()):
    print("Parola este puternica")
else:
    print("Parola este slaba")