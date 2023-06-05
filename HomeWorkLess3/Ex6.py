"""
 Extrageți un subșir de caractere
Scrieți un program care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator.
"""

sir = input("Introdu un șir de caractere: ")
inceput = input("Introdu poziția de început: ")
sfarsit = input("Introdu poziția de sfârșit: ")

subsir = sir[inceput-1:sfarsit]

print(f"Subșirul specific este: {subsir}")

