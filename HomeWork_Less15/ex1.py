import os

def list_files_in_directory(path):
    if not os.path.exists(path):
        print("Calea introdusă nu există.")
        return

    if not os.path.isdir(path):
        print("Calea introdusă nu este un director.")
        return

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        print(file)

# Exemplu de utilizare
directory_path = input("Introduceți calea directorului: ")
list_files_in_directory(directory_path)
