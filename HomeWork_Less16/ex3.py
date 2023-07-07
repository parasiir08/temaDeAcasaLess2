def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print(f"Fisierul {file_path} a fost creat cu succes.")
    except Exception as e:
        print(f"A apărut o eroare la crearea fișierului: {str(e)}")

def write_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text)
            print("Textul a fost adăugat în fișier.")
    except Exception as e:
        print(f"A apărut o eroare la scrierea în fișier: {str(e)}")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Conținutul fișierului {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"Fisierul {file_path} nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare la citirea fișierului: {str(e)}")

# Exemplu de utilizare
file_path = input("Introduceți numele fișierului: ")
create_file(file_path)

text = input("Introduceți textul pe care doriți să îl adăugați în fișier: ")
write_to_file(file_path, text)

print("Citirea din fișier:")
read_file(file_path)
