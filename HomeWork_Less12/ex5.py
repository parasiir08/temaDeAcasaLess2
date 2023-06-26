'''Scrieți o funcție Python numită is_valid_email care validează formatul unei adrese de email date.
Funcția ar trebui să primească un singur argument: email (șir de caractere) care reprezintă adresa de email de validat.
Funcția ar trebui să returneze o valoare booleană care indică dacă adresa de email este validă.

Criteriile de validare ale adresei de email sunt următoarele:

Conține un singur simbol "@".
Conține cel puțin un punct (.) după simbolul "@".
Domeniul (după ultimul punct) are cel puțin două caractere.
Scrieți un program care utilizează funcția is_valid_email pentru a face următoarele:

Solicitați utilizatorului să introducă o adresă de email.
Apelați funcția is_valid_email cu valoarea introdusă.
Afișați dacă adresa de email este validă sau nu.
'''

def check_password_strength(password: str):
    if "@" in password:
        index = password.index("@")
        if "." in password[index:]:
            domain = password[index+1:]
            last_dot_index = domain.rindex(".")
            domain_extension = domain[last_dot_index+1:]
            if len(domain_extension) >= 2:
                return print(True)
            else:
                return print(False)
        else:
            return print(True)
    else:
        return print(False)
parola = input("Introdu parola ta: ")
check_password_strength(parola)

