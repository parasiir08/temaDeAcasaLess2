def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Conținutul fișierului {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"Fisierul {file_path} nu a fost gasit.")
    except Exception as e:
        print(f"A aparut o eroare la citirea fisierului: {str(e)}")

# Exemplu de utilizare
file_path = "/Users/parasiir08/Downloads/ex_2_file.txt"
read_file(file_path)
