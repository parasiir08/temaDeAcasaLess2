'''
Scrieți un program care afișează numerele de la 1 la 100.
Pentru multiplii de 3, se va afișa "Fizz" în locul numărului.
Pentru multiplii de 5, se va afișa "Buzz".
Pentru numerele care sunt multipli atât de 3, cât și de 5, se va afișa " FizzBuzz".
'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

