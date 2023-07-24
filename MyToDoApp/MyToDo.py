
from prettytable import PrettyTable
print("\nMy ToDo List")
#Instructiuni pentru ToDoList
instructions = ("1.Insert a to add\n2.Insert d to delete\n3.Insert u to update the list\n4.Insert e to exit\n5.Insert L to show the list")
print(instructions)
#Creez lista mea
my_todo_list = []
#Creez o functie pentru a adauga valori
x = PrettyTable()
def my_list():
    x.field_names = ["Item Names"]
    for i in my_todo_list:
        #Cu linia de mai jos adaugam un rind nou la pretytable cu fiecare iteratie
        x.add_row([i])
        #Linia de mai jos va da un titlu tabelului
    print(x.get_string(title= "To do list"))
    #De fiecare data cind acest table se va incarca, va sterge toate valorile din el
    # si va face update la lista mea cu informatie noua
    x.clear_rows()

running = True
while running:
    #primi valori de la utilizator
    user_input = input("\nWhat do you want to do? (A, D, U, E, L)").lower()
    if user_input == "a":
        new_todo = input("\nPlease enter your new ToDo ")
        print(f"\nYour current ToDO is {new_todo}.")
        #adaug noul todo la lista noastra
        my_todo_list.append(new_todo)
    #Creez un nou while loop, care va face loop pina cind userul va introduce valid value
    elif user_input == "d":
        while True:
            #intrebam utilizatorul sa introduca o valoare valida
            item_name = input("\nPlease enter a name of a value you want to delete").lower()
            #aici folosim try catch pentru a exclude orice exceptie
            try:
                #Verificam daca itemul este prezent in ToDo List
                if item_name in my_todo_list:
                    #acum asteptam utilizatorul sa confirme.
                    choice = input(f"Are you sure to delete {item_name}? (Y/N)").lower()
                    if choice == "y":
                        #eliminam elementeul din todo list
                        my_todo_list.remove(item_name)
                        print("Your updated To-DO List. ")
                        my_list()
                        #Stopam loop aic
                        break
                else:
                    print("Item was not found")
            except Exception:
                print("Something went wrong")
    elif user_input == "u":
        #acelasi cod ca delete doar cu mici schimbari
        #primul while loop
        while True:
            item_name = input("\nPlease enter a name of an item you want to update").lower()
            try:
                #Verificam daca elementul este in lista
                if item_name in my_todo_list:
                        #intrebam utilizatorul pentru confirmare
                    choice = input(f"Are you sure to update {item_name} from To-DO List? (Y/N)").lower()
                    if choice == "y":
                        update_item = input(f"Please enter a name you want to update {item_name} with. ").lower()
                        #Primim indexul la itemul care vrem sa-l inlocuim
                        index = my_todo_list.index(item_name)
                        #replace the item
                        my_todo_list[index] = update_item
                        my_list()
                        #termianm loop
                        break
                else:
                    print("Item not found.")
            except Exception:
                    print("Something went wrong")
    elif user_input == "e":
        pass
    elif user_input == "l":
        pass
    elif user_input == "" or user_input == " ":
        print("Please enter something")
    else:
        print("Enter a valid value")

