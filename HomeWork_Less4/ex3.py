"""
Citiţi de la tastatură un număr întreg.
Dacă numărul este negativ, afişaţi mesajul `"That number is less than 0!"`.
Dacă este pozitiv, afişaţi `"That number is greater than 0!"`.
Dacă nu este nici negativ nici pozitiv afişaţi mesajul `"You picked 0!"`.
"""
numar_intreg=int(input("Introdu un numar intreg"))
if numar_intreg<0:
    print("Numarul este mai mic ca 0")
elif numar_intreg>0:
    print("Numarul este mai mare ca 0")
else:
    print("Ai ales 0")


