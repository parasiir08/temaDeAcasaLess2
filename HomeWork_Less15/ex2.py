import os
import shutil

def get_creation_time(file_path):
    return os.path.getctime(file_path)

def rename_files_with_prefix(directory_path, prefix=""):
    if not os.path.exists(directory_path):
        print("Calea introdusă nu există.")
        return

    if not os.path.isdir(directory_path):
        print("Calea introdusă nu este un director.")
        return

    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    files.sort(key=get_creation_time)

    count = 1
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        new_file_name = f"{prefix}{count}{file_ext}"
        new_file_path = os.path.join(directory_path, new_file_name)
        old_file_path = os.path.join(directory_path, file)
        shutil.move(old_file_path, new_file_path)
        count += 1

# Exemplu de utilizare
folder_path = input("Introduceți calea directoriei: ")
prefix = input("Introduceți prefixul (lăsați gol pentru a nu utiliza prefixul): ")

rename_files_with_prefix(folder_path, prefix)
