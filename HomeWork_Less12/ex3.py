'''
Scrieți o funcție Python numită check_password_strength
care verifică puterea unei parole date. Funcția ar trebui să primească
un singur argument: password (șir de caractere) care reprezintă parola de verificat.
Funcția ar trebui să returneze o valoare booleană care indică
dacă parola respectă criteriile de putere specificate.

Criteriile de putere ale parolei sunt următoarele:
Cel puțin 8 caractere lungime
Conține cel puțin o literă majusculă
Conține cel puțin o literă minusculă
Conține cel puțin o cifră
Conține cel puțin un caracter special (de exemplu, !@#$%^&*)
Scrieți un program care utilizează funcția check_password_strength pentru a face următoarele:

Solicitați utilizatorului să introducă o parolă.
Apelați funcția check_password_strength cu valoarea introdusă.
Afișați dacă parola respectă criteriile de putere sau nu.
'''

def check_password_strength(password: str):
    special_characters = "#$!@%^&*"

    uppercase_present = False
    lowercase_present = False
    digit_present = False
    special_character_present = False

    for char in password:
        if char.isupper():
            uppercase_present = True
        elif char.islower():
            lowercase_present = True
        elif char.isdigit():
            digit_present = True
        elif char in special_characters:
            special_character_present = True

    if not uppercase_present:
        print("Parola nu conține cel puțin o literă majusculă")
    if not lowercase_present:
        print("Parola nu conține cel puțin o literă minusculă")
    if not digit_present:
        print("Parola nu conține cel puțin un număr")
    if not special_character_present:
        print("Parola nu conține cel puțin un caracter special")
    if len(password) < 8:
        print("Parola conține mai puțin de 8 caractere")
    else:
        print("Parola conține cel puțin 8 caractere")

    if uppercase_present and lowercase_present and digit_present and special_character_present and len(password) >= 8:
        return "Parola este scrisă după toate regulile"
    else:
        return "Parola nu este suficient de puternică"

parola = input("Introdu parola ta: ")
print(check_password_strength(parola))
