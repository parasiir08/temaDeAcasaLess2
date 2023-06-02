#Exercițiul 7: Calculatorul de dobândă simplă
#Scrie un program care preia suma principală, rata dobânzii și timpul (în ani) ca intrare.
# Calculează și afișează dobânda simplă folosind formula: dobândă = (suma principală * rată dobândă * timp) / 100.

suma = int(input("Introdu suma principala "))
rata = float(input("Introdu rata dobinzii "))
timp = int(input("Introdu timpul in ani "))

calcule = (suma * rata * timp) / 100
print(f"Dobinda simpla este: {calcule}")

