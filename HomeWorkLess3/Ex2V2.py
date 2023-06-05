sir = input("Introdu un sir de caractere: ")
sir = sir.lower()

numar_total_litere = len(sir)
numar_vocale = sum(sir.count(vocala) for vocala in 'aeiouăîâ')
numar_consoane = numar_total_litere - numar_vocale

print(f"Numarul total de litere: {numar_total_litere}")
print(f"Numarul de vocale: {numar_vocale}")
print(f"Numarul de consoane: {numar_consoane}")
