def get_age():
    try:
        age = int(input("Introdu vârsta ta: "))

        if age < 0 or age > 150:
            raise ValueError("Vârsta trebuie să fie între 0 și 150")

        return age

    except ValueError as ex:
        raise ValueError("Vârsta trebuie să fie un număr întreg") from ex

try:
    varsta = get_age()
    print("Vârsta ta este:", varsta)

except ValueError as ex:
    print(ex)
