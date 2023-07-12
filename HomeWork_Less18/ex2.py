'''
Creati un decorator care verifica daca valoare returnata de functia care o decoreaza mereu e un numar.

Functia trebuie sa fie numita validate_numeric si va produce ValueError cand functia nu intoarce valoare numerica.
'''

def validate_numeric(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise ValueError(f"Valoarea returnată de {func.__name__} nu este numerică.")
        return result
    return wrapper

@validate_numeric
def input_numeric(prompt):
    return float(input(prompt))

try:
    b = input_numeric("Introdu ceva text: ")
    print(f"{b} este un număr.")
except ValueError as e:
    print(str(e))


