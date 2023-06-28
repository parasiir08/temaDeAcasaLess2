def factorial(numar):
    if not isinstance(numar, int) or numar < 0:
        raise ValueError("Numărul trebuie să fie un număr întreg pozitiv")

    rezultat = 1
    for i in range(1, numar + 1):
        rezultat *= i

    return rezultat


try:
    numar = int(input("Introdu un număr întreg pozitiv: "))
    rezultat_factorial = factorial(numar)
    print("Factorialul numărului", numar, "este:", rezultat_factorial)

except ValueError as ex:
    print(ex)
