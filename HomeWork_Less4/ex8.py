"""
Scrieți un program care cere utilizatorului să introducă o propoziție.
Dacă propoziția se încheie cu un semn de întrebare ("?"),
afișați mesajul „Aceasta este o întrebare”.
În caz contrar, afișați mesajul „Aceasta nu este o întrebare”
"""
propozitie = input("Introdu o propozitie ")
if "?" in propozitie[-1]:
    print("Aceasta este o intrebare")
else:
    print("Aceasta nu este o intrebare")
