'''
Scrieți un program care utilizează o buclă while pentru a calcula factorialul unui număr întreg pozitiv dat n.
Factorialul unui număr este produsul tuturor numerelor întregi pozitive de la 1 la n.
'''

numar = int(input("Introduceți un număr întreg pozitiv: "))

if numar < 0:
    print("Nu se poate calcula factorialul pentru un număr negativ.")
else:
    factorial_val = 1
    i = 1

    while i <= numar:
        factorial_val *= i
        i += 1

    print("Factorialul numărului", numar, "este:", factorial_val)
