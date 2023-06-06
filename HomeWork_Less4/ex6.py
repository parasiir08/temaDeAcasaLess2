"""
Scrieţi un program care citeşte de la tastatură numele unei persoane.
Dacă numele nu începe cu literă mare, atunci programul transformă valoarea citită în numele persoanei scris cu literă mare.
După aceasta, afişează la ecran `"Salut, <numele citit de la tastatura care începe cu litera mare>!"`.
"""
nume=input("Introdu numele tau ")
if nume[0].islower():
    nume= nume[0].capitalize() + nume[1:]
    print(f"Salut, {nume}")
else:
    print(f"Salut, {nume}")

