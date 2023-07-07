def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print(f"Fisierul {file_path} a fost creat cu succes.")
    except Exception as e:
        print(f"A apărut o eroare la crearea fișierului: {str(e)}")

# Exemplu de utilizare
file_path = input("Introduceți numele sau calea fișierului: ")
create_file(file_path)
