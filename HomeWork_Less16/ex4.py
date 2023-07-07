def display_dishes(dishes):
    if not dishes:
        print("Nu există bucate în lista.")
    else:
        print("Bucatele disponibile sunt:")
        for dish in dishes:
            print(dish)

def save_dishes_to_file(dishes, file_path):
    try:
        with open(file_path, 'w') as file:
            for dish in dishes:
                file.write(dish + '\n')
        print(f"Bucatele au fost salvate în fișierul {file_path}.")
    except Exception as e:
        print(f"A apărut o eroare la salvarea bucatelor în fișier: {str(e)}")

def add_dish(dishes, dish_name):
    dishes.append(dish_name)
    print(f"Bucata '{dish_name}' a fost adăugată.")

def load_dishes_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            dishes = file.read().splitlines()
        print(f"Bucatele au fost încărcate din fișierul {file_path}.")
        return dishes
    except FileNotFoundError:
        print(f"Fisierul {file_path} nu a fost găsit.")
        return []
    except Exception as e:
        print(f"A apărut o eroare la încărcarea bucatelor din fișier: {str(e)}")
        return []

# Exemplu de utilizare
file_path = "dishes.txt"
dishes = load_dishes_from_file(file_path)

choice = ""

while choice != "q":
    print("\nOpțiuni disponibile:")
    print("1. Afișează toate bucatele")
    print("2. Adaugă o bucătă")
    print("3. Salvează bucatele în fișier")
    print("q. Ieșire din program")

    choice = input("Introduceți opțiunea dorită: ")

    if choice == "1":
        display_dishes(dishes)
    elif choice == "2":
        dish_name = input("Introduceți numele bucății: ")
        add_dish(dishes, dish_name)
    elif choice == "3":
        save_dishes_to_file(dishes, file_path)
    elif choice == "q":
        print("Programul a fost încheiat.")
    else:
        print("Opțiune invalidă. Vă rugăm să încercați din nou.")

